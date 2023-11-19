from __future__ import annotations

import concurrent.futures

import rich.console

import lea


def test(
    client: lea.clients.Client,
    views_dir: str,
    select: list[str],
    threads: int,
    fail_fast: bool,
    console: rich.console.Console,
):
    # List all the columns
    columns = client.get_columns()
    # HACK: we should have a cleaner way to handle schemas/views irrespective of the client
    if hasattr(client, "dataset_name"):
        columns["view_name"] = f"{client.dataset_name}." + columns["view_name"]

    # The client determines where the views will be written

    # List singular tests
    views = lea.views.load_views(views_dir, sqlglot_dialect=client.sqlglot_dialect)
    singular_tests = [view for view in views if view.schema == "tests"]
    console.log(f"Found {len(singular_tests):,d} singular tests")

    # List assertion tests
    assertion_tests = []
    for view in filter(lambda v: v.schema not in {"funcs", "tests"}, views):
        view_columns = columns.query(f"view_name == '{client._make_view_path(view)}'")[
            "column"
        ].tolist()
        for test in client.discover_assertion_tests(view=view, view_columns=view_columns):
            assertion_tests.append(test)
    console.log(f"Found {len(assertion_tests):,d} assertion tests")

    # Determine which tests need to be run
    tests = singular_tests + assertion_tests
    blacklist = set(t.key for t in tests).difference(select) if select else set()
    console.log(f"{len(tests) - len(blacklist):,d} test(s) selected")
    tests = [test for test in tests if test.key not in blacklist]

    # Run tests concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        jobs = {executor.submit(client.load, test): test for test in tests}
        for job in concurrent.futures.as_completed(jobs):
            test = jobs[job]
            conflicts = job.result()
            if conflicts.empty:
                console.log(f"SUCCESS {test}", style="bold green")
            else:
                console.log(f"FAILURE {test}", style="bold red")
                console.log(conflicts.head())
                if fail_fast:
                    # TODO: print out the query to help quick debugging
                    raise RuntimeError(f"Test {test} failed")
