"""query commands for cmem command line interface."""
import json
import re
import sys
from hashlib import sha1
from shutil import get_terminal_size
from json import JSONDecodeError, load
from time import sleep, time
from typing import Dict, List, Optional
from uuid import uuid4

import click

from requests import HTTPError

from cmem.cmemc.cli import completion
from cmem.cmemc.cli.commands import CmemcCommand, CmemcGroup
from cmem.cmemc.cli.context import ApplicationContext
from cmem.cmemc.cli.utils import extract_error_message, struct_to_table
from cmem.cmempy.queries import (
    QUERY_CATALOG, SparqlQuery, cancel_query, get_query_status
)

QUERY_FILTER_TYPES = sorted(
    ['graph', 'status', 'slower-than', 'type', 'regex', 'trace-id', 'user']
)
QUERY_FILTER_HELP_TEXT = (
    "Filter queries based on execution status and time. "
    f"First parameter --filter CHOICE can be one of {str(QUERY_FILTER_TYPES)}"
    ". The second parameter is based on CHOICE, e.g. int in case of"
    " slower-than, or a regular expression string."
)


class ReplayStatistics:
    """Capture and calculate statistics of a query replay command run."""

    # pylint: disable=too-many-instance-attributes
    runId: str = str(uuid4())
    query_minimum: int = None   # type: ignore
    query_maximum: int = None   # type: ignore
    loop_count: int = 0
    loop_durations: Dict[str, int] = {}
    query_durations: Dict[str, List[int]] = {}
    current_loop_key: str = None   # type: ignore
    total_duration: int = 0
    query_count: int = 0
    error_count: int = 0
    query_average: float = None   # type: ignore
    catalog = QUERY_CATALOG
    app: ApplicationContext = None   # type: ignore

    def __init__(self, app, label: Optional[str] = None):
        """Initialize instance."""
        self.app = app
        self.label = label

    def init_loop(self) -> str:
        """Initialize a new loop and reset the loop counts/values."""
        loop_key = str(uuid4())
        self.current_loop_key = loop_key
        self.loop_durations[loop_key] = 0
        self.query_durations[loop_key] = []
        self.loop_count += 1
        self.app.echo_debug(f"Loop {self.loop_count} started: {loop_key}")
        return loop_key

    def _init_query(self, query_: dict) -> SparqlQuery:
        """Initialize query from dict."""
        try:
            if "iri" in query_.keys():
                iri = query_["iri"]
                catalog_entry = self.catalog.get_query(iri)
                if catalog_entry is None:
                    raise ValueError(
                        f"measure_query - query {iri} is not in catalog."
                    )
                return catalog_entry
            query_string = query_["queryString"]
            return SparqlQuery(text=query_string)
        except KeyError as error:
            raise ValueError(
                "measure_query - given input dict has no queryString key."
            ) from error

    def _update_statistic_on_success(self, duration: int):
        """Update statistics and counters."""
        self.query_durations[self.current_loop_key].append(duration)
        if self.query_minimum is None or duration < self.query_minimum:
            self.query_minimum = duration
        if self.query_maximum is None or duration > self.query_maximum:
            self.query_maximum = duration
        self.total_duration += duration
        self.loop_durations[self.current_loop_key] += duration
        self.query_average = self.total_duration / self.query_count

    def measure_query_duration(self, query_: dict) -> dict:
        """Execute a query and measure the duration."""
        # create the query object
        executed_query = self._init_query(query_)

        # update and return the query object
        if "id" not in query_.keys():
            # create a UUID4, if needed
            query_["id"] = str(uuid4())
        # always re-hash
        query_["queryStringSha1Hash"] = sha1(  # nosec
            executed_query.text.encode('utf-8')
        ).hexdigest()
        if "queryString" not in query_.keys():
            # add queryString for catalog queries
            query_["queryString"] = executed_query.text
        if "iri" in query_.keys():
            # use the full IRI in case short one is given
            query_["iri"] = executed_query.url
        if "iri" in query_.keys() and "label" not in query_.keys():
            # extend with label if possible (and needed)
            query_["label"] = executed_query.label
        if "replays" not in query_.keys():
            # create replays object if needed
            query_["replays"] = []

        # init replay object
        this_replay = {
            "runId": str(self.runId),
            "loopId": str(self.current_loop_key),
            "replayId": str(uuid4()),
        }
        if self.label is not None:
            this_replay["runLabel"] = self.label

        # execute and measure the query
        try:
            start = round(time() * 1000)
            executed_query.get_results(replace_placeholder=False)
            self.query_count += 1
            end = round(time() * 1000)
            duration = end - start

            this_replay["executionStarted"] = str(start)
            this_replay["executionFinished"] = str(end)
            this_replay["executionTime"] = str(duration)

            # update statistics and counters
            self._update_statistic_on_success(duration)
        except HTTPError as error:
            self.error_count += 1
            this_replay["executionError"] = extract_error_message(error)

        query_["replays"].append(this_replay)
        self.app.echo_debug(
            f"Query {self.query_count + self.error_count} "
            f"executed: {this_replay['replayId']}"
        )
        return query_

    def create_output(self):
        """Create the structure for the output commands."""
        output = {}
        for key, value in vars(self).items():
            if key not in ("current_loop_key", "app"):
                # ignore some object vars on output
                output[key] = value
        loop_average = 0
        loop_minimum = None
        loop_maximum = None
        for loop_duration in self.loop_durations.values():
            loop_average += loop_duration
            if loop_minimum is None or loop_duration < loop_minimum:
                loop_minimum = loop_duration
            if loop_maximum is None or loop_duration > loop_maximum:
                loop_maximum = loop_duration
        output["loop_minimum"] = loop_minimum
        output["loop_maximum"] = loop_maximum
        output["loop_average"] = loop_average / len(self.loop_durations)
        return output

    def output_table(self):
        """Output a table of the statistic values."""
        table = struct_to_table(self.create_output())
        self.app.echo_info_table(
            table,
            headers=["Key", "Value"],
            sort_column=0
        )

    def output_json(self):
        """Output json of the statistic values."""
        self.app.echo_info_json(self.create_output())


def _get_queries_filtered_by_type(queries, query_type: str):
    """Get queries filter by query type.

    Args:
        query_type (str): the type of the query

    Returns:
        filtered list of status reports

    Raises:
        ValueError
    """
    filtered_queries = []
    try:
        for _ in queries:
            if _["type"].lower() == query_type.lower():
                filtered_queries.append(_)
    except KeyError as error:
        raise NotImplementedError(
            "Filtering queries by type needs DataPlatform >= 22.1"
        ) from error
    return filtered_queries


def _get_queries_filtered_by_slower_than(queries, time_ms):
    """Get queries filter by slower-than x ms filter.

    Args:
        time_ms: time in milliseconds

    Returns:
        filtered list of status reports

    Raises:
        ValueError
    """
    try:
        time_ms = int(time_ms)
    except ValueError as error:
        raise ValueError("This filter needs an integer as parameter.") \
            from error
    return [
        _ for _ in queries
        if _.get("executionTime", 0) > time_ms
    ]


def _get_queries_filtered_by_status(
        queries: List[Dict], status: str
):  # noqa: C901
    """Get queries filter by a status.

    Args:
        status (str): one of error, running, finished

    Returns:
        filtered list of status reports

    Raises:
        ValueError
    """
    # check for correct filter names (filter ids is used internally only)

    valid_filter_values = (
        "running", "finished", "error", "cancelled", "timeout"
    )
    status = status.lower()
    if status not in valid_filter_values:
        raise ValueError(
            f"This filter needs one of {valid_filter_values} as parameter."
        )
    filtered_queries = []
    if status == "running":
        filtered_queries = [
            _ for _ in queries
            if _["queryExecutionState"] == "RUNNING"
        ]
    if status == "finished":
        filtered_queries = [
            _ for _ in queries
            if _["queryExecutionState"].startswith("FINISHED")
        ]
    # error -> List only queries which were NOT successfully executed.
    # interpreted as: do not include timeout and cancelled queries
    if status == "error":
        filtered_queries = [
            _ for _ in queries
            if _["queryExecutionState"] == "FINISHED_ERROR"
        ]
    if status == "cancelled":
        filtered_queries = [
            _ for _ in queries
            if _["queryExecutionState"] == "FINISHED_CANCELLED"
        ]
    if status == "timeout":
        filtered_queries = [
            _ for _ in queries
            if _["queryExecutionState"] == "FINISHED_TIMEOUT"
        ]
    return filtered_queries


def _get_queries_filtered_by_uuid(queries, uuid):
    """Get query status by uuid.

    Args:
        uuid (str): query status uuid

    Returns:
        status dict
    """
    filtered_queries = []
    for _ in queries:
        if _["id"] == uuid:
            filtered_queries.append(_)
    return filtered_queries


def _get_queries_filtered(
        queries: List[Dict],
        filter_name: str, filter_value: str
):
    """Get queries filtered according to filter name and value.

    Args:
        queries: List[Dict]: List of query results
        filter_name (str): one of "status" or "slower-than"
        filter_value (str|int): value according to filter

    Returns:
        list of filtered queries from the get_query_status API call

    Raises:
        ValueError
    """
    # filter by uuid
    if filter_name == "uuid":
        return _get_queries_filtered_by_uuid(queries, filter_value)
    # check for correct filter names (filter ids is used internally only)
    if filter_name not in QUERY_FILTER_TYPES:
        raise ValueError(
            f"{filter_name} is an unknown filter name. "
            f"Use one of {QUERY_FILTER_TYPES}."
        )
    filtered_queries = []
    # filter by status
    if filter_name == "status":
        filtered_queries = _get_queries_filtered_by_status(
            queries, filter_value
        )
    # filter by slower-than
    if filter_name == "slower-than":
        filtered_queries = _get_queries_filtered_by_slower_than(
            queries, filter_value
        )
    # filter by type
    if filter_name == "type":
        filtered_queries = _get_queries_filtered_by_type(
            queries, filter_value
        )
    # filter by regex
    if filter_name == "regex":
        filtered_queries = [
            _ for _ in queries
            if re.search(filter_value, _["queryString"])
        ]
    # filter by traceID
    if filter_name == "trace-id":
        filtered_queries = [
            _ for _ in queries
            if _.get("traceId", None) == filter_value
        ]
    # filter by user
    if filter_name == "user":
        filtered_queries = [
            _ for _ in queries
            if _.get("user", None) == filter_value
        ]
    # filter by user
    if filter_name == "graph":
        if filter_value == "":
            filtered_queries = [
                _ for _ in queries
                if not _.get("affectedGraphs", [])
            ]
        else:
            filtered_queries = [
                _ for _ in queries
                if filter_value in _.get("affectedGraphs", [])
            ]
    # default is unfiltered
    return filtered_queries


def _output_query_status_details(app: ApplicationContext, status_dict):
    """Output key/value table as well as query string of a query.

    Args:
        status_dict (dict): The dict from the query status list.
    """
    table = []
    for key in status_dict.keys():
        if key != "queryString":
            row = [
                key,
                str(status_dict[key])
            ]
            table.append(row)
    app.echo_info_table(
        table,
        headers=["Key", "Value"],
        sort_column=0
    )
    app.echo_info("")
    app.echo_info_sparql(status_dict["queryString"])


@click.command(cls=CmemcCommand, name="list")
@click.option(
    "--id-only",
    is_flag=True,
    help="Lists only query identifier and no labels or other metadata. "
         "This is useful for piping the ids into other cmemc commands."
)
@click.pass_obj
def list_command(app, id_only):
    """List available queries from the catalog.

    Outputs a list of query URIs which can be used as reference for
    the query execute command.
    """
    queries = QUERY_CATALOG.get_queries().items()
    if id_only:
        # sort dict by short_url - https://docs.python.org/3/howto/sorting.html
        for _, sparql_query in sorted(
                queries, key=lambda k: k[1].short_url.lower()
        ):
            app.echo_info(
                sparql_query.short_url
            )
    else:
        table = []
        for _, sparql_query in queries:
            row = [
                sparql_query.short_url,
                sparql_query.query_type,
                ','.join(sparql_query.get_placeholder_keys()),
                sparql_query.label
            ]
            table.append(row)
        app.echo_info_table(
            table,
            headers=["Query URI", "Type", "Placeholder", "Label"],
            sort_column=3
        )


# pylint: disable-msg=too-many-locals,too-many-arguments
@click.command(cls=CmemcCommand, name="execute")
@click.argument(
    "QUERIES",
    nargs=-1,
    required=True,
    shell_complete=completion.remote_queries_and_sparql_files
)
@click.option(
    "--accept",
    default="default",
    show_default=True,
    help="Accept header for the HTTP request(s). Setting this to 'default' "
         "means that cmemc uses an appropriate accept header for terminal "
         "output (text/csv for tables, text/turtle for graphs, * otherwise). "
         "Please refer to the Corporate Memory system manual for a list "
         "of accepted mime types."
)
@click.option(
    "--no-imports",
    is_flag=True,
    help="Graphs which include other graphs (using owl:imports) will be "
         "queried as merged overall-graph. This flag disables this "
         "default behaviour. The flag has no effect on update queries."
)
@click.option(
    "--base64",
    is_flag=True,
    help="Enables base64 encoding of the query parameter for the "
         "SPARQL requests (the response is not touched). "
         "This can be useful in case there is an aggressive firewall between "
         "cmemc and Corporate Memory."
)
@click.option(
    "--parameter", "-p",
    type=(str, str),
    shell_complete=completion.placeholder,
    multiple=True,
    help="In case of a parameterized query (placeholders with the '{{key}}' "
         "syntax), this option fills all placeholder with a given value "
         "before the query is executed."
         "Pairs of placeholder/value need to be given as a tuple 'KEY VALUE'. "
         "A key can be used only once."
)
@click.option(
    "--limit",
    type=int,
    help="Override or set the LIMIT in the executed SELECT query. Note that "
         "this option will never give you more results than the LIMIT given "
         "in the query itself."
)
@click.option(
    "--offset",
    type=int,
    help="Override or set the OFFSET in the executed SELECT query."
)
@click.option(
    "--distinct",
    is_flag=True,
    help="Override the SELECT query by make the result set DISTINCT."
)
@click.option(
    "--timeout",
    type=int,
    help="Set max execution time for query evaluation (in milliseconds)."
)
@click.pass_obj
def execute_command(
        app, queries, accept, no_imports, base64, parameter,
        limit, offset, distinct, timeout
):
    """Execute queries which are loaded from files or the query catalog.

    Queries are identified either by a file path, a URI from the query
    catalog, or a shortened URI (qname, using a default namespace).

    If multiple queries are executed one after the other, the first failing
    query stops the whole execution chain.

    Limitations: All optional parameters (e.g. accept, base64, ...) are
    provided for ALL queries in an execution chain. If you need different
    parameters for each query in a chain, run cmemc multiple times and use
    the logical operators && and || of your shell instead.
    """
    # pylint: disable=too-many-arguments
    placeholder = {}
    for key, value in parameter:
        if key in placeholder:
            raise ValueError(
                "Parameter can be given only once, "
                f"Value for '{key}' was given twice."
            )
        placeholder[key] = value
    app.echo_debug("Parameter: " + str(placeholder))
    for file_or_uri in queries:
        app.echo_debug(
            f"Start of execution: {file_or_uri} with "
            f"placeholder {placeholder}"
        )
        executed_query = QUERY_CATALOG.get_query(
            file_or_uri, placeholder=placeholder
        )
        if executed_query is None:
            raise ValueError(
                f"{file_or_uri} is neither a (readable) file nor a query URI."
            )
        app.echo_debug(
            f"Execute ({executed_query.query_type}): "
            f"{executed_query.label} < {executed_query.url}"
        )
        if accept == "default":
            submitted_accept = executed_query.get_default_accept_header()
            app.echo_debug(
                f"Accept header set to default value: '{submitted_accept}'"
            )
        else:
            submitted_accept = accept

        results = executed_query.get_results(
            accept=submitted_accept,
            owl_imports_resolution=not no_imports,
            base64_encoded=base64,
            placeholder=placeholder,
            distinct=distinct,
            limit=limit,
            offset=offset,
            timeout=timeout
        )
        app.echo_result(results)


@click.command(cls=CmemcCommand, name="open")
@click.argument(
    "QUERIES",
    nargs=-1,
    required=True,
    shell_complete=completion.remote_queries_and_sparql_files
)
@click.pass_obj
def open_command(app, queries):
    """Open queries in the editor of the query catalog in your browser.

    With this command, you can open (remote) queries from the query catalog in
    the query editor in your browser (e.g. in order to change them).
    You can also load local query files into the query editor, in order to
    import them into the query catalog.

    The command accepts multiple query URIs or files which results in
    opening multiple browser tabs.
    """
    for file_or_uri in queries:
        opened_query = QUERY_CATALOG.get_query(file_or_uri)
        if opened_query is None:
            raise ValueError(
                f"{file_or_uri} is neither a (readable) file nor a query URI."
            )
        open_query_uri = opened_query.get_editor_url()
        app.echo_debug(f"Open {file_or_uri}: {open_query_uri}")
        click.launch(open_query_uri)


@click.command(cls=CmemcCommand, name="status")
@click.option(
    "--id-only",
    is_flag=True,
    help="Lists only query identifier and no labels or other metadata. "
         "This is useful for piping the ids into other cmemc commands."
)
@click.option(
    "--raw",
    is_flag=True,
    help="Outputs raw JSON response of the query status API."
)
@click.option(
    "--filter", "filter_",
    type=(str, str),
    multiple=True,
    shell_complete=completion.query_status_filter,
    help=QUERY_FILTER_HELP_TEXT,
)
@click.argument(
    "query_uuid",
    required=False,
    type=click.STRING
)
@click.pass_obj
def status_command(app, id_only, raw, filter_, query_uuid):
    """Get status information of executed and running queries.

    With this command, you can access the latest executed SPARQL queries
    on the DataPlatform. These queries are identified by UUIDs and listed
    ordered by starting timestamp.

    You can filter queries based on status and runtime in order to investigate
    slow queries. In addition to that, you can get the details of a specific
    query by using the ID as a parameter.
    """
    width, height = get_terminal_size((120, 20))
    max_query_string_width = width - 46 - 1
    app.echo_debug(f"Terminal size = {width} x {height}")

    queries = get_query_status()
    if query_uuid:
        queries = _get_queries_filtered(queries, "uuid", query_uuid)

    for _ in filter_:
        filter_type, filter_name = _
        queries = _get_queries_filtered(queries, filter_type, filter_name)
    if raw:
        app.echo_info_json(queries)
        return
    if id_only:
        for _ in queries:
            app.echo_info(_["id"])
        return
    if len(queries) == 1 and query_uuid:
        _output_query_status_details(app, queries[0])
        return
    table = []
    for _ in queries:
        query_string = " ".join(_["queryString"].splitlines())
        if len(query_string) > max_query_string_width:
            query_string = query_string[0:max_query_string_width] + "…"
        row = [
            _["id"],
            _["executionTime"],
            query_string
        ]
        table.append(row)
    app.echo_info_table(
        table,
        headers=["Query ID", "Time", "Query String"]
    )


@click.command(cls=CmemcCommand, name="replay")
@click.argument(
    "REPLAY_FILE",
    required=True,
    shell_complete=completion.replay_files,
    type=click.Path(
        exists=True,
        allow_dash=False,
        readable=True,
        dir_okay=False
    )
)
@click.option(
    "--raw",
    is_flag=True,
    help="Output the execution statistic as raw JSON."
)
@click.option(
    "--loops",
    required=False,
    default=1,
    show_default=True,
    type=int,
    help="Number of loops to run the replay file."
)
@click.option(
    "--wait",
    required=False,
    default=0,
    show_default=True,
    type=int,
    help="Number of seconds to wait between query executions."
)
@click.option(
    "--output-file",
    required=False,
    shell_complete=completion.replay_files,
    help="Save the optional output to this file. Input and output of the "
         "command can be the same file. The output is written at the end "
         "of a successful command execution. The output can be stdout "
         "('-') - in this case, the execution statistic output is "
         "oppressed.",
    type=click.Path(
        exists=False,
        allow_dash=True,
        writable=True,
        dir_okay=False
    )
)
@click.option(
    "--run-label",
    type=click.STRING,
    help="Optional label of this replay run."
)
@click.pass_obj
def replay_command(
        app, replay_file, raw, loops, wait, output_file, run_label
):
    """Re-execute queries from a replay file.

    This command reads a REPLAY_FILE and re-executes the logged queries.
    A REPLAY_FILE is a JSON document which is an array of JSON objects with
    at least a key `queryString` holding the query text OR a key `iri`
    holding the IRI of the query in the query catalog.
    It can be created with the `query status` command.

    Example: query status --raw > replay.json

    The output of this command shows basic query execution statistics.

    The queries are executed one after another in the order given in the
    input REPLAY_FILE. Query placeholders / parameters are ignored. If a
    query results in an error, the duration is not counted.

    The optional output file is the same JSON document which is used as input,
    but each query object is annotated with an additional `replays` object,
    which is an array of JSON objects which hold values for the
    replay|loop|run IDs, start and end time as well as duration and
    other data.
    """
    try:
        with open(replay_file, 'r', encoding='utf8') as _:
            input_queries = load(_)
    except JSONDecodeError as error:
        raise ValueError(
            f"File {replay_file} is not a valid JSON document."
        ) from error
    if len(input_queries) == 0:
        raise ValueError(
            f"File {replay_file} contains no queries."
        )
    app.echo_debug(
        f"File {replay_file} contains {len(input_queries)} queries."
    )
    statistic = ReplayStatistics(app=app, label=run_label)
    for _loop in range(loops):
        statistic.init_loop()
        for _ in input_queries:
            _ = statistic.measure_query_duration(_)
            if wait > 0:
                sleep(wait)

    if output_file:
        if output_file == "-":
            app.echo_info_json(input_queries)
            return
        with open(output_file, 'w', encoding='utf-8') as output:
            json.dump(input_queries, output, ensure_ascii=False, indent=2)

    if raw:
        statistic.output_json()
    else:
        statistic.output_table()


@click.command(cls=CmemcCommand, name="cancel")
@click.argument(
    "query_id",
    required=True,
    type=click.STRING
)
@click.pass_obj
def cancel_command(app: ApplicationContext, query_id):
    """Cancel a running query.

    With this command, you can cancel a running query.
    Depending on the backend triple store, this will result in a
    broken result stream (stardog, neptune and virtuoso) or a valid
    result stream with incomplete results (graphdb)
    """
    app.echo_info(f"Cancel query {query_id} ... ", nl=False)
    queries = get_query_status()
    queries = _get_queries_filtered(queries, "uuid", query_id)
    if not queries:
        app.echo_error("not known (anymore)")
        sys.exit(1)
    queries = _get_queries_filtered(queries, "status", "running")
    if not queries:
        app.echo_error("not running anymore")
        sys.exit(1)
    cancel_query(queries[0]["id"])
    app.echo_success("done")


@click.group(cls=CmemcGroup)
def query():
    """List, execute, get status or open SPARQL queries.

    Queries are identified either by a file path, a URI from the query
    catalog or a shortened URI (qname, using a default namespace).

    One or more queries can be executed one after the other with the
    execute command. With open command you can jump to the query editor in your
    browser.

    Queries can use a mustache like syntax to specify placeholder for
    parameter values (e.g. {{resourceUri}}). These parameter values need to
    be given as well, before the query can be executed (use the -p option).

    Note: In order to get a list of queries from the query catalog, execute
    the `query list` command or use tab-completion.
    """


query.add_command(execute_command)
query.add_command(list_command)
query.add_command(open_command)
query.add_command(status_command)
query.add_command(replay_command)
query.add_command(cancel_command)
