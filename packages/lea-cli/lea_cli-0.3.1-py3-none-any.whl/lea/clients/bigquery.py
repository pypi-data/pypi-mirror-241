from __future__ import annotations

import os

import pandas as pd
import sqlglot

import lea

from .base import AssertionTag, Client


class BigQuery(Client):
    def __init__(self, credentials, location, project_id, dataset_name, username):
        from google.cloud import bigquery

        self.project_id = project_id
        self.location = location
        self.client = bigquery.Client(credentials=credentials)
        self._dataset_name = dataset_name
        self.username = username

    def prepare(self, views, console):
        dataset = self.create_dataset()
        console.log(f"Created dataset {dataset.dataset_id}")

    @property
    def sqlglot_dialect(self):
        return sqlglot.dialects.Dialects.BIGQUERY

    @property
    def dataset_name(self):
        return f"{self._dataset_name}_{self.username}" if self.username else self._dataset_name

    def create_dataset(self):
        from google.cloud import bigquery

        dataset_ref = bigquery.DatasetReference(
            project=self.project_id, dataset_id=self.dataset_name
        )
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = self.location
        dataset = self.client.create_dataset(dataset, exists_ok=True)
        return dataset

    def teardown(self):
        from google.cloud import bigquery

        dataset_ref = self.client.dataset(self.dataset_name)
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = self.location
        self.client.delete_dataset(dataset, delete_contents=True, not_found_ok=True)

    def _make_job(self, view: lea.views.SQLView):
        query = view.query.replace(f"{self._dataset_name}.", f"{self.dataset_name}.")

        return self.client.create_job(
            {
                "query": {
                    "query": query,
                    "destinationTable": {
                        "projectId": self.project_id,
                        "datasetId": self.dataset_name,
                        "tableId": f"{self._make_view_path(view).split('.', 1)[1]}",
                    },
                    "createDisposition": "CREATE_IF_NEEDED",
                    "writeDisposition": "WRITE_TRUNCATE",
                },
                "labels": {
                    "job_dataset": self.dataset_name,
                    "job_schema": view.schema,
                    "job_table": f"{self._make_view_path(view).split('.', 1)[1]}",
                    "job_username": self.username,
                    "job_is_github_actions": "GITHUB_ACTIONS" in os.environ,
                },
            }
        )

    def _create_sql_view(self, view: lea.views.SQLView):
        job = self._make_job(view)
        job.result()

    def _create_python_view(self, view: lea.views.PythonView):
        from google.cloud import bigquery

        dataframe = self._load_python_view(view)

        job_config = bigquery.LoadJobConfig(
            schema=[],
            write_disposition="WRITE_TRUNCATE",
        )

        job = self.client.load_table_from_dataframe(
            dataframe,
            f"{self.project_id}.{self._make_view_path(view)}",
            job_config=job_config,
        )
        job.result()

    def _render_view_query(self, view: lea.views.SQLView) -> str:
        query = view.query
        if self.username:
            query = query.replace(f"{self._dataset_name}.", f"{self.dataset_name}.")
        return query

    def _load_sql_view(self, view: lea.views.SQLView) -> pd.DataFrame:
        query = self._render_view_query(view)
        return pd.read_gbq(query, credentials=self.client._credentials)

    def list_existing_view_names(self):
        return {
            tuple(table.table_id.split("__")): table.table_id.split("__", 1)
            for table in self.client.list_tables(self.dataset_name)
        }

    def delete_view(self, view: lea.views.View):
        self.client.delete_table(f"{self.project_id}.{self._make_view_path(view)}")

    def get_tables(self):
        query = f"""
        SELECT
            table_name AS view_name,
            total_rows AS n_rows,
            total_logical_bytes AS n_bytes
        FROM `region-{self.location.lower()}`.INFORMATION_SCHEMA.TABLE_STORAGE_BY_PROJECT
        WHERE table_schema = '{self.dataset_name}'
        """
        view = lea.views.GenericSQLView(
            schema=None, name=None, query=query, sqlglot_dialect=self.sqlglot_dialect
        )
        return self._load_sql_view(view)

    def get_columns(self) -> pd.DataFrame:
        query = f"""
        SELECT
            table_name AS view_name,
            column_name AS column,
            data_type AS type
        FROM {self.dataset_name}.INFORMATION_SCHEMA.COLUMNS
        """
        view = lea.views.GenericSQLView(
            schema=None, name=None, query=query, sqlglot_dialect=self.sqlglot_dialect
        )
        columns = self._load_sql_view(view)
        return columns

    def _make_view_path(self, view: lea.views.View) -> str:
        return f"{self.dataset_name}.{lea._SEP.join(view.key)}"

    def make_column_test_unique(self, view: lea.views.View, column: str) -> str:
        return self.load_assertion_test_template(AssertionTag.UNIQUE).render(
            table=self._make_view_path(view), column=column
        )

    def make_column_test_unique_by(self, view: lea.views.View, column: str, by: str) -> str:
        schema, *leftover = view.key
        return self.load_assertion_test_template(AssertionTag.UNIQUE_BY).render(
            table=self._make_view_path(view), column=column, by=by
        )

    def make_column_test_no_nulls(self, view: lea.views.View, column: str) -> str:
        schema, *leftover = view.key
        return self.load_assertion_test_template(AssertionTag.NO_NULLS).render(
            table=self._make_view_path(view), column=column
        )

    def make_column_test_set(self, view: lea.views.View, column: str, elements: set[str]) -> str:
        schema, *leftover = view.key
        return self.load_assertion_test_template(AssertionTag.SET).render(
            table=self._make_view_path(view), column=column, elements=elements
        )
