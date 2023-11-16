"""Utility functions for CLI auto-completion functionality."""
# pylint: disable=unused-argument, broad-except, too-many-lines
import os
from collections import Counter
from contextlib import suppress

from click import Context
from click.parser import split_arg_string
from click.shell_completion import CompletionItem
from natsort import natsorted, ns
from prometheus_client.parser import text_string_to_metric_families

from cmem.cmemc.cli.context import CONTEXT
from cmem.cmemc.cli.utils import (
    get_graphs,
    metric_get_labels,
    metrics_get_dict, struct_to_table, get_published_packages
)
from cmem.cmempy.dp.admin import get_prometheus_data
from cmem.cmempy.health import get_complete_status_info
from cmem.cmempy.keycloak.client import list_open_id_clients
from cmem.cmempy.keycloak.group import list_groups
from cmem.cmempy.keycloak.user import list_users, get_user_by_username, user_groups
from cmem.cmempy.plugins.marshalling import get_marshalling_plugins
from cmem.cmempy.queries import QUERY_CATALOG, get_query_status
from cmem.cmempy.vocabularies import get_vocabularies
from cmem.cmempy.workflow.workflows import get_workflows_io
from cmem.cmempy.workspace import (
    get_task_plugin_description,
    get_task_plugins,
)
from cmem.cmempy.workspace.projects.project import get_projects
from cmem.cmempy.workspace.projects.resources import get_all_resources
from cmem.cmempy.workspace.projects.variables import get_all_variables
from cmem.cmempy.workspace.python import list_packages
from cmem.cmempy.workspace.search import list_items

from cmem.cmempy.workspace.projects.datasets.dataset import get_dataset

SORT_BY_KEY = 0
SORT_BY_DESC = 1


def _finalize_completion(
        candidates: list,
        incomplete: str = '',
        sort_by: int = SORT_BY_KEY,
        nat_sort: bool = False,
        reverse: bool = False
) -> list:
    """Sort and filter candidates list.

    candidates are sorted with natsort library by sort_by key.

    Args:
        candidates (list):  completion dictionary to filter
        incomplete (str):   incomplete string at the cursor
        sort_by (str):      SORT_BY_KEY or SORT_BY_DESC
        nat_sort (bool):    if true, uses the natsort package for sorting
        reverse (bool):     if true, sorts in reverse order

    Returns:
        filtered and sorted candidates list

    Raises:
        ValueError in case of wrong sort_by parameter
    """
    if sort_by not in (SORT_BY_KEY, SORT_BY_DESC):
        raise ValueError("sort_by should be 0 or 1.")
    incomplete = incomplete.lower()
    if len(candidates) == 0:
        return candidates
    # remove duplicates
    candidates = list(set(candidates))
    if isinstance(candidates[0], str):
        # list of strings filtering and sorting
        filtered_candidates = [
            element for element in candidates
            if element.lower().find(incomplete) != -1
        ]
        if nat_sort:
            return natsorted(
                seq=filtered_candidates,
                alg=ns.IGNORECASE,
                reverse=reverse
            )
        # this solves that case-insensitive sorting is not stable in ordering
        # of "equal" keys (https://stackoverflow.com/a/57923460)
        return sorted(
            filtered_candidates,
            key=lambda x: (str(x).casefold(), x),
            reverse=reverse
        )
    if isinstance(candidates[0], tuple):
        # list of tuples filtering and sorting
        filtered_candidates = [
            element for element in candidates
            if str(element[0]).lower().find(incomplete) != -1
            or str(element[1]).lower().find(incomplete) != -1
        ]
        if nat_sort:
            sorted_list = natsorted(
                seq=filtered_candidates,
                key=lambda k: k[sort_by],   # type: ignore
                alg=ns.IGNORECASE,
                reverse=reverse
            )
        else:
            sorted_list = sorted(
                filtered_candidates,
                key=lambda x: (str(x[sort_by]).casefold(), str(x[sort_by])),
                reverse=reverse
            )
        return [
            CompletionItem(
                value=element[0].replace(":", r"\:"),
                help=element[1]
            ) for element in sorted_list
        ]
    raise ValueError(
        "candidates should be a list of strings or a list of tuples."
    )


def _get_completion_args(incomplete):
    """get completion args

    This is a workaround to get partial tuple options in a completion function
    see https://github.com/pallets/click/issues/2597
    """
    args = split_arg_string(os.environ["COMP_WORDS"])
    if incomplete and len(args) > 0 and args[len(args)-1] == incomplete:
        args.pop()
    return args


def _ignore_option(option, params):
    """
    Check if the given 'option' is present in the 'params' dictionary
    or any of its values.
    """
    ignore_project_id = False
    for _ in params:
        if hasattr(params[_], '__iter__') and option in params[_]:
            ignore_project_id = True
        elif option == params[_]:
            ignore_project_id = True

    return ignore_project_id


def add_metadata_parameter(list_=None):
    """Extend a list with metadata keys and key descriptions."""
    if list_ is None:
        list_ = []
    list_.insert(
        0,
        ("description", "Metadata: A description.")
    )
    list_.insert(
        0,
        ("label", "Metadata: A name.")
    )
    return list_


def add_read_only_and_uri_property_parameters(list_=None):
    """Extend a list with readonly/uriProperty keys and key descriptions."""
    if list_ is None:
        list_ = []
    list_.append(
        (
            "readOnly",
            "Read-only: If enabled, all write operations using this dataset object "
            "will fail, e.g. when used as output in workflows or transform/linking "
            "executions. This will NOT protect the underlying resource in general, "
            "e.g. files, databases or knowledge graphs could still be changed "
            "externally."
         )
    )
    list_.append(
        (
            "uriProperty",
            "URI attribute: When reading data from the dataset, the specified "
            "attribute will be used to get the URIs of the entities. "
            "When writing to a dataset, the specified attribute will be automatically "
            "added to the schema as well as the generated entity URIs will be added as "
            "values for each entity. If the entered value is not a valid URI, "
            "it will be converted to a valid URI."
        )
    )
    return list_


def dataset_parameter(ctx, param, incomplete):
    """Prepare a list of dataset parameters for a dataset type."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    args = _get_completion_args(incomplete)
    incomplete = incomplete.lower()
    # look if cursor is in value position of the -p option and
    # return nothing in case it is (values are not completed atm)
    if args[len(args) - 2] in ("-p", "--parameter"):
        return []
    # try to determine the dataset type
    dataset_type = ctx.params.get('dataset_type')
    if dataset_type is None:
        try:
            dataset_id = ctx.args[0]
            project = get_dataset(
                project_name=dataset_id.split(":")[0],
                dataset_name=dataset_id.split(":")[1]
            )
            dataset_type = project["data"]["type"]
        except IndexError:
            pass

    # without type, we know nothing
    if dataset_type is None:
        return []
    plugin = get_task_plugin_description(dataset_type)
    properties = plugin["properties"]
    options = []
    for key in properties:
        title = properties[key]["title"]
        description = properties[key]["description"]
        option = f"{title}: {description}"
        options.append((key, option))

    options = add_read_only_and_uri_property_parameters(options)
    # sorting: metadata on top, then parameter per key
    options = sorted(options, key=lambda k: k[0].lower())
    options = add_metadata_parameter(options)
    # restrict to search
    options = [
        key for key in options
        if (key[0].lower().find(incomplete.lower()) != -1
            or key[1].lower().find(incomplete.lower()) != -1
            )
    ]

    return [CompletionItem(value=option[0], help=option[1]) for option in options]


def dataset_types(ctx, param, incomplete):
    """Prepare a list of dataset types."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    incomplete = incomplete.lower()
    options = []
    plugins = get_task_plugins()
    for plugin_id in plugins:
        plugin = plugins[plugin_id]
        title = plugin["title"]
        description = plugin["description"].partition("\n")[0]
        option = f"{title}: {description}"
        if plugin["taskType"] == "Dataset" and (
                plugin_id.lower().find(incomplete.lower()) != -1
                or option.lower().find(incomplete.lower()) != -1):
            options.append(
                (
                    plugin_id,
                    option
                )
            )
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def dataset_ids(ctx, param, incomplete):
    """Prepare a list of projectid:datasetid dataset identifier."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []
    results = list_items(item_type="dataset")
    datasets = results["results"]
    for _ in datasets:
        options.append(
            (
                _['projectId'] + ":" + _['id'],
                _["label"]
            )
        )
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete
    )


def dataset_list_filter(ctx, param, incomplete):
    """Prepare a list of filter names and values for dataset list filter."""
    filter_names = [
        (
            "project",
            "Filter by project ID."
        ),
        (
            "regex",
            "Filter by regular expression on the dataset label."
        ),
        (
            "tag",
            "Filter by tag label."
        ),
        (
            "type",
            "Filter by dataset type."
        ),
    ]
    filter_regex = [
        (
            r"^Final\:",
            "Example: Dataset label starts with 'Final:'."
        ),
        (
            r"[12][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]",
            "Example: Dataset label contains a data-like string."
        )
    ]
    options = []
    args = _get_completion_args(incomplete)
    if args[len(args) - 1] == "--filter":
        options = _finalize_completion(
            candidates=filter_names,
            incomplete=incomplete
        )
    if args[len(args) - 1] == "type":
        options = dataset_types(ctx, param, incomplete)
    if args[len(args) - 1] == "project":
        options = project_ids(ctx, param, incomplete)
    if args[len(args) - 1] == "tag":
        options = tag_labels(ctx, param, incomplete, "dataset")
    if args[len(args) - 1] == "regex":
        options = _finalize_completion(
            candidates=filter_regex,
            incomplete=incomplete
        )
    return options


def resource_ids(ctx, param, incomplete):
    """Prepare a list of projectid:resourceid resource identifier."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []
    for _ in get_all_resources():
        options.append(
            (
                _["id"]
            )
        )
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def scheduler_ids(ctx, param, incomplete):
    """Prepare a list of projectid:schedulerid scheduler identifier."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []
    schedulers = list_items(
        item_type="task",
        facets=[{
            "facetId": "taskType",
            "keywordIds": ["Scheduler"],
            "type": "keyword"
        }]
    )["results"]
    for _ in schedulers:
        if _ignore_option(_["projectId"] + ":" + _["id"], ctx.params):
            continue
        options.append(
            (
                _["projectId"] + ":" + _["id"],
                _["label"]
            )
        )
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def metric_ids(ctx, param, incomplete):
    """Prepare a list of metric identifier."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []

    data = get_prometheus_data().text
    for family in text_string_to_metric_families(data):
        options.append(
            (
                family.name,
                family.documentation
            )
        )
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_KEY
    )


def metric_label_filter(ctx, param, incomplete):
    """Prepare a list of label name or values."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    args = _get_completion_args(incomplete)
    incomplete = incomplete.lower()
    options = []
    metric_id = ctx.args[0]
    labels = metric_get_labels(metrics_get_dict()[metric_id])
    if args[len(args) - 1] in "--filter":
        # we are in the name position
        options = labels.keys()
    if args[len(args) - 2] in "--filter":
        label_name = args[len(args) - 1]
        # we are in the value position
        options = labels[label_name]
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_KEY
    )


def vocabularies(ctx, param, incomplete, filter_="all"):
    """Prepare a list of vocabulary graphs for auto-completion."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []
    try:
        vocabs = get_vocabularies(filter_=filter_)
    except Exception:
        # if something went wrong, die silently
        return []
    for _ in vocabs:
        url = _["iri"]
        if _ignore_option(url, ctx.params):
            continue
        url = _["iri"]
        try:
            label = _["label"]["title"]
        except (KeyError, TypeError):
            label = "Vocabulary in graph " + url
        options.append((url, label))
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def installed_vocabularies(ctx, param, incomplete):
    """Prepare a list of installed vocabulary graphs."""
    return vocabularies(ctx, param, incomplete, filter_="installed")


def installable_vocabularies(ctx, param, incomplete):
    """Prepare a list of installable vocabulary graphs."""
    return vocabularies(ctx, param, incomplete, filter_="installable")


def file_list(incomplete="", suffix="", description="", prefix=""):
    """Prepare a list of files with specific parameter."""
    directory = os.getcwd()
    options = []
    for file_name in os.listdir(directory):
        if os.path.isfile(file_name) \
                and file_name.endswith(suffix) \
                and file_name.startswith(prefix):
            options.append((file_name, description))
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_KEY
    )


def workflow_io_ids(ctx, param, incomplete):
    """Prepare a list of io workflows."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []
    for _ in get_workflows_io():
        workflow_id = _["projectId"] + ":" + _["id"]
        label = _["label"]
        options.append((workflow_id, label))
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def replay_files(ctx, param, incomplete):
    """Prepare a list of JSON replay files."""
    return file_list(
        incomplete=incomplete,
        suffix=".json",
        description="JSON query replay file"
    )


def installed_package_names(ctx, param, incomplete):
    """Prepare a list of installed packages."""
    CONTEXT.set_connection_from_args(ctx.find_root().params)
    options = []
    packages = list_packages()
    for _ in packages:
        options.append(
            (
                _["name"],
                _["version"]
            )
        )
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_KEY
    )


def published_package_names(ctx, param, incomplete):
    """List of plugin packages scraped from pypi.org."""
    options = []
    for _ in get_published_packages():
        options.append(
            (
                _.name,
                f"{_.version}: {_.description}"
            )
        )

    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_KEY
    )


def python_package_files(ctx, param, incomplete):
    """Prepare a list of acceptable python package files."""
    return file_list(
        incomplete=incomplete,
        suffix=".tar.gz",
        description="Plugin Python Package file",
        prefix="cmem-plugin-"
    )


def installable_packages(ctx, param, incomplete):
    """Installable packages from files and pypi.org."""
    return python_package_files(
        ctx, param, incomplete) + published_package_names(
        ctx, param, incomplete)


def workflow_io_input_files(ctx, param, incomplete):
    """Prepare a list of acceptable workflow io input files."""
    return file_list(
        incomplete=incomplete,
        suffix=".csv",
        description="CSV Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".xml",
        description="XML Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".json",
        description="JSON Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".xlsx",
        description="Excel Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".txt",
        description="Text Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".zip",
        description="Multi CSV Dataset resource"
    )


def workflow_io_input_mimetypes(ctx, args, incomplete):
    """Prepare a list of acceptable workflow io input mimetypes."""
    return file_list(
        incomplete=incomplete,
        suffix=".csv",
        description="CSV Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".xml",
        description="XML Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".json",
        description="JSON Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".xlsx",
        description="Excel Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".txt",
        description="Text Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".zip",
        description="Multi CSV Dataset resource"
    )


def workflow_io_output_files(ctx, param, incomplete):
    """Prepare a list of acceptable workflow io output files."""
    return file_list(
        incomplete=incomplete,
        suffix=".csv",
        description="CSV Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".xml",
        description="XML Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".json",
        description="JSON Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".xlsx",
        description="Excel Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".ttl",
        description="RDF file Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".nt",
        description="RDF file Dataset resource"
    )


def dataset_files(ctx, param, incomplete):
    """Prepare a list of SPARQL files."""
    return file_list(
        incomplete=incomplete,
        suffix=".csv",
        description="CSV Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".xlsx",
        description="Excel Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".xml",
        description="XML Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".json",
        description="JSON Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".ttl",
        description="RDF file Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".zip",
        description="multiCsv Dataset resource"
    ) + file_list(
        incomplete=incomplete,
        suffix=".orc",
        description="Apache ORC Dataset resource"
    )


def graph_backup_files(ctx, param, incomplete):
    """Prepare a list of workspace files."""
    return file_list(
        incomplete=incomplete,
        suffix=".graphs.zip",
        description="eccenca Corporate Memory graph backup file"
    )


def project_files(ctx, param, incomplete):
    """Prepare a list of workspace files."""
    return file_list(
        incomplete=incomplete,
        suffix=".project.zip",
        description="eccenca Corporate Memory project backup file"
    )


def ini_files(ctx, param, incomplete):
    """Prepare a list of workspace files."""
    return file_list(
        incomplete=incomplete,
        suffix=".ini",
        description="INI file"
    )


def workspace_files(ctx, param, incomplete):
    """Prepare a list of workspace files."""
    return file_list(
        incomplete=incomplete,
        suffix=".workspace.zip",
        description="eccenca Corporate Memory workspace backup file"
    )


def sparql_files(ctx, param, incomplete):
    """Prepare a list of SPARQL files."""
    return file_list(
        incomplete=incomplete,
        suffix=".sparql",
        description="SPARQL query file"
    ) + file_list(
        incomplete=incomplete,
        suffix=".rq",
        description="SPARQL query file"
    )


def triple_files(ctx, param, incomplete):
    """Prepare a list of triple files."""
    return file_list(
        incomplete=incomplete,
        suffix=".ttl",
        description="RDF Turtle file"
    ) + file_list(
        incomplete=incomplete,
        suffix=".nt",
        description="RDF NTriples file"
    )


def placeholder(ctx, param, incomplete):
    """Prepare a list of placeholder from the to-be executed queries."""
    # look if cursor is in value position of the -p option and
    # return nothing in case it is (values are not completed atm)
    args = _get_completion_args(incomplete)
    if args[len(args) - 2] in ("-p", "--parameter"):
        return []
    # setup configuration
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    # extract placeholder from given queries in the command line
    options = []
    for num, arg in enumerate(args):
        query = QUERY_CATALOG.get_query(arg)
        if query is not None:
            options.extend(
                list(query.get_placeholder_keys())
            )
    # look for already given parameter in the arguments and remove them from
    # the available options
    for num, arg in enumerate(args):
        if num - 1 > 0 and args[num - 1] in ("-p", "--parameter"):
            options.remove(arg)
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete
    )


def remote_queries(ctx, param, incomplete):
    """Prepare a list of query URIs."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []
    for _, query in QUERY_CATALOG.get_queries().items():
        url = query.short_url
        label = query.label
        options.append((url, label))
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def remote_queries_and_sparql_files(ctx, param, incomplete):
    """Prepare a list of named queries, query files and directories."""
    remote = remote_queries(ctx, param, incomplete)
    files = sparql_files(ctx, param, incomplete)
    return remote + files


def workflow_ids(ctx, param, incomplete):
    """Prepare a list of projectid:taskid workflow identifier."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    workflows = list_items(item_type="workflow")["results"]
    options = []
    for _ in workflows:
        workflow = _["projectId"] + ":" + _["id"]
        label = _["label"]
        if _ignore_option(workflow, ctx.params):
            continue
        options.append((workflow, label))
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def marshalling_plugins(ctx, param, incomplete):
    """Prepare a list of supported workspace/project import/export plugins."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = get_marshalling_plugins()
    if "description" in options[0].keys():
        final_options = [(_["id"], _["description"]) for _ in options]
    else:
        # in case, no descriptions are available, labels are fine as well
        final_options = [(_["id"], _["label"]) for _ in options]

    return _finalize_completion(
        candidates=final_options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def project_ids(ctx, param, incomplete):
    """Prepare a list of project IDs for auto-completion."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    try:
        projects = get_projects()
    except Exception:
        # if something went wrong, die silently
        return []
    options = []
    for _ in projects:
        project_id = _["name"]
        label = _["metaData"]["label"]
        # do not add project if already in the command line
        if _ignore_option(project_id, ctx.params):
            continue
        options.append((project_id, label))
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def graph_uris(ctx, param, incomplete, writeable=True, readonly=True):
    """Prepare a list of graphs for auto-completion."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    try:
        graphs = get_graphs()
    except Exception:
        # if something went wrong, die silently
        return []
    options = []
    for _ in graphs:
        iri = _["iri"]
        label = _["label"]["title"]
        # do not add graph if already in the command line
        if _ignore_option(iri, ctx.params):
            continue
        options.append((iri, label))
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def writable_graph_uris(ctx, param, incomplete):
    """Prepare a list of writable graphs for auto-completion."""
    return graph_uris(ctx, param, incomplete, writeable=True, readonly=False)


def connections(ctx, param, incomplete):
    """Prepare a list of config connections for auto-completion."""
    # since ctx does not have an obj here, we re-create the object
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []
    for section in CONTEXT.config.sections():
        options.append(section)
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete
    )


def graph_export_templates(ctx, param, incomplete):
    """Prepare a list of example templates for the graph export command."""
    examples = [
        (
            "{{hash}}",
            "Example: 6568a[...]00b08.ttl"
        ),
        (
            "{{iriname}}",
            "Example: https__ns_eccenca_com_data_config.ttl"
        ),
        (
            "{{date}}-{{iriname}}",
            "Example: 2021-11-29-https__ns_eccenca_com_data_config.ttl"
        ),
        (
            "{{date}}-{{connection}}-{{iriname}}",
            "Example: 2021-11-29-mycmem-https__ns_eccenca_com_data_config.ttl"
        ),
    ]
    return _finalize_completion(
        candidates=examples,
        incomplete=incomplete
    )


def project_export_templates(ctx, param, incomplete):
    """Prepare a list of example templates for the project export command."""
    examples = [
        (
            "{{id}}",
            "Example: a plain file name"
        ),
        (
            "{{date}}-{{connection}}-{{id}}.project",
            "Example: a more descriptive file name"),
        (
            "dumps/{{connection}}/{{id}}/{{date}}.project",
            "Example: a whole directory tree"
        )
    ]
    return _finalize_completion(
        candidates=examples,
        incomplete=incomplete
    )


def workspace_export_templates(ctx, param, incomplete):
    """Prepare a list of example templates for the workspace export command."""
    examples = [
        (
            "workspace",
            "Example: a plain file name"
        ),
        (
            "{{date}}-{{connection}}.workspace",
            "Example: a more descriptive file name"),
        (
            "dumps/{{connection}}/{{date}}.workspace",
            "Example: a whole directory tree"
        )
    ]
    return _finalize_completion(
        candidates=examples,
        incomplete=incomplete
    )


def query_status_filter(ctx, param, incomplete):
    """Prepare a list of filter names and values for query status filter."""
    filter_names = [
        (
            "status",
            "List only queries which have a certain status "
            "(cancelled, running, finished or error)."
        ),
        (
            "slower-than",
            "List only queries which are slower than X milliseconds."
        ),
        (
            "type",
            "List only queries of a certain query type."
        ),
        (
            "regex",
            "List only queries which query text matches a regular expression."
        ),
        (
            "trace-id",
            "List only queries which have the specified trace ID."
        ),
        (
            "user",
            "List only queries executed by the specified account (URL)."
        ),
        (
            "graph",
            "List only queries which affected a certain graph (URL)."
        ),
    ]
    filter_regex = [
        (
            r"http\:\/\/schema.org",
            "List only queries which somehow use the schema.org namespace."
        ),
        (
            r"http\:\/\/www.w3.org\/2000\/01\/rdf-schema\#",
            "List only queries which somehow use the RDF schema namespace."
        ),
        (
            r"\\\?value",
            "List only queries which are using the ?value projection variable."
        ),
        (
            "^CREATE SILENT GRAPH",
            "List only queries which start with CREATE SILENT GRAPH."
        )
    ]
    filter_status = [
        (
            "running",
            "List only queries which are currently running."
        ),
        (
            "finished",
            "List only queries which are not running anymore."
        ),
        (
            "error",
            "List only queries which were NOT successfully executed."
        ),
        (
            "cancelled",
            "List only queries which were cancelled."
        ),
        (
            "timeout",
            "List only queries which ran into a timeout."
        )
    ]
    filter_slower = [
        (
            "5",
            "List only queries which are executed slower than 5ms."
        ),
        (
            "100",
            "List only queries which are executed slower than 100ms."
        ),
        (
            "1000",
            "List only queries which are executed slower than 1000ms."
        ),
        (
            "5000",
            "List only queries which are executed slower than 5000ms."
        )
    ]
    filter_type = [
        (
            "ASK",
            "Queries, which return a boolean indicating whether a query "
            "pattern matches or not."
        ),
        (
            "SELECT",
            "Queries, which returns all, or a subset of, the variables "
            "bound in a query pattern match."
        ),
        (
            "DESCRIBE",
            "Queries, which return an RDF graph that describes the "
            "resources found."
        ),
        (
            "CONSTRUCT",
            "Queries, which return an RDF graph constructed by substituting "
            "variables in a set of triple templates."
        ),
        (
            "UPDATE", "Queries, which modify one or more graphs "
                      "(INSERT, DELETE, DROP, etc.)."
        ),
        (
            "UNKNOWN",
            "Queries of unknown type."
        )
    ]
    args = _get_completion_args(incomplete)
    last_argument = args[len(args) - 1]
    options = None
    if last_argument == "--filter":
        options = _finalize_completion(
            candidates=filter_names,
            incomplete=incomplete
        )
    if last_argument == "regex":
        options = _finalize_completion(
            candidates=filter_regex,
            incomplete=incomplete
        )
    if last_argument == "status":
        options = _finalize_completion(
            candidates=filter_status,
            incomplete=incomplete
        )
    if last_argument == "slower-than":
        options = _finalize_completion(
            candidates=filter_slower,
            incomplete=incomplete,
            nat_sort=True
        )
    if last_argument == "type":
        options = _finalize_completion(
            candidates=filter_type,
            incomplete=incomplete
        )
    if last_argument == "user":
        options = query_account_iris(ctx, param, incomplete)
    if last_argument == "trace-id":
        options = query_trace_ids(ctx, param, incomplete)
    if last_argument == "graph":
        options = query_graphs(ctx, param, incomplete)

    if not options:
        raise ValueError(
            "Last argument unknown. Can not do completion."
        )
    return options


def query_account_iris(ctx, param, incomplete):
    """Prepare a list account IRIs from the query status."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    accounts = {}
    for _ in get_query_status():
        if _["user"] in accounts:
            accounts[_["user"]] += 1
        else:
            accounts[_["user"]] = 1
    options = [
        (account, f"{count} queries")
        for account, count in accounts.items()
    ]
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete
    )


def query_trace_ids(ctx, param, incomplete):
    """Prepare a list trace IDs from the query status."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = Counter(
        [query["traceId"] for query in get_query_status()]
    ).most_common()
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def query_graphs(ctx, param, incomplete):
    """Prepare a list graph URLs from the query status."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = Counter()
    for query in get_query_status():
        for graph in query.get("affectedGraphs", []):
            options.update([graph.replace(":", r"\:")])
    return _finalize_completion(
        candidates=options.most_common(),
        incomplete=incomplete,
        sort_by=SORT_BY_KEY
    )


def graph_list_filter(ctx, param, incomplete):
    """Prepare a list of filter names and values for graph list filter."""
    filter_names = [
        (
            "access",
            "List only graphs which have a certain access condition "
            "(readonly or writeable)."
        ),
        (
            "imported-by",
            "List only graphs which are in the import tree of a "
            "specified graph."
        )
    ]
    filter_values_access = [
        (
            "readonly",
            "List only graphs which are NOT writable for the current user."
        ),
        (
            "writeable",
            "List only graphs which ARE writeable for the current user."
        )
    ]
    args = _get_completion_args(incomplete)
    options = []
    if args[len(args) - 1] == "--filter":
        options = _finalize_completion(
            candidates=filter_names,
            incomplete=incomplete
        )
    if args[len(args) - 1] == "access":
        options = _finalize_completion(
            candidates=filter_values_access,
            incomplete=incomplete
        )
    if args[len(args) - 1] == "imported-by":
        options = graph_uris(ctx, param, incomplete)
    return options


def variable_ids(ctx, param, incomplete):
    """Prepare a list of variables IDs for auto-completion."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    try:
        variables = get_all_variables()
    except Exception:
        # if something went wrong, die silently
        return []
    options = []
    for _ in variables:
        variable_id = _["id"]
        label = _.get("description", "").partition('\n')[0]
        if label == "":
            label = f"Current value: {_['value']}"
        # do not add project if already in the command line
        if _ignore_option(variable_id, ctx.params):
            continue
        options.append((variable_id, label))
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_KEY
    )


def variable_list_filter(ctx, param, incomplete):
    """Prepare a list of filter names and values for variable list filter."""
    filter_names = [
        (
            "project",
            "Filter for variables from a specific project."
        ),
        (
            "regex",
            "Filter for variables with a regular expression search over "
            "id, value and description."
        )
    ]
    filter_values_regex = [
        (
            "ending$",
            "Variables name ends with 'ending'."
        ),
        (
            "^starting",
            "Variables name starts with 'starting'."
        )
    ]
    args = _get_completion_args(incomplete)
    if args[len(args) - 1] == "--filter":
        return [CompletionItem(value=f[0], help=f[1]) for f in filter_names]
    if args[len(args) - 1] == "regex":
        return _finalize_completion(
            candidates=filter_values_regex,
            incomplete=incomplete
        )
    if args[len(args) - 1] == "project":
        return project_ids(ctx, param, incomplete)
    return []


def resource_list_filter(ctx, param, incomplete):
    """Prepare a list of filter names and values for resource list filter."""
    filter_names = [
        (
            "project",
            "Filter for file resources from a specific project."
        ),
        (
            "regex",
            "Filter for file resources with a regular expression search on "
            "the name field."
        )
    ]
    filter_values_regex = [
        (
            "csv$",
            "File resources which name ends with .csv"
        ),
        (
            "2021-10-[0-9][0-9]",
            "File resources which name has a date from 2021-10 in it"
        )
    ]
    args = _get_completion_args(incomplete)
    if args[len(args) - 1] == "--filter":
        return [CompletionItem(value=f[0], help=f[1]) for f in filter_names]
    if args[len(args) - 1] == "project":
        return _finalize_completion(
            candidates=project_ids(ctx, param, incomplete),
            incomplete=incomplete
        )
    if args[len(args) - 1] == "regex":
        return _finalize_completion(
            candidates=filter_values_regex,
            incomplete=incomplete
        )
    return []


def workflow_list_filter(ctx, param, incomplete):
    """Prepare a list of filter names and values for workflow list filter."""
    filter_names = [
        (
            "project",
            "Filter by project ID."
        ),
        (
            "io",
            "Filter by workflow io feature."
        ),
        (
            "regex",
            "Filter by regular expression on the workflow label."
        ),
        (
            "tag",
            "Filter by tag label."
        ),
    ]
    filter_values_io = [
        (
            "any",
            "List all workflows suitable for the io command."
        ),
        (
            "input-only",
            "List only workflows with a variable input dataset."
        ),
        (
            "output-only",
            "List only workflows with a variable output dataset."
        ),
        (
            "input-output",
            "List only workflows with a variable input and output dataset."
        ),
    ]
    filter_regex = [
        (
            r"^Final\:",
            "Example: Workflow label starts with 'Final:'."
        ),
        (
            r"[12][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]",
            "Example: Workflow label contains a data-like string."
        )
    ]
    options = []
    args = _get_completion_args(incomplete)
    if args[len(args) - 1] == "--filter":
        options = filter_names
    if args[len(args) - 1] == "io":
        options = filter_values_io
    if args[len(args) - 1] == "project":
        options = project_ids(ctx, param, incomplete)
    if args[len(args) - 1] == "tag":
        options = tag_labels(ctx, param, incomplete, "workflow")
    if args[len(args) - 1] == "regex":
        options = filter_regex

    if len(options) > 0 and isinstance(options[0], CompletionItem):
        return options

    return _finalize_completion(
        candidates=options,
        incomplete=incomplete
    )


def tag_labels(ctx, param, incomplete, item_type):
    """Prepare a list of tag labels for a item_type."""
    datasets = list_items(item_type=item_type)
    options = []
    counts = {}
    for _dataset in datasets["results"]:
        for _tag in _dataset["tags"]:
            if _tag["label"] in counts:
                counts[_tag["label"]] += 1
            else:
                counts[_tag["label"]] = 1
    for tag, count in counts.items():
        options.append((tag, f"{count} item(s): {tag}"))
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC,
        reverse=True
    )


def status_keys(ctx, param, incomplete):
    """Prepare a list of status keys for the admin status command."""
    options = ["all"]
    os.environ["CMEMPY_IS_CHATTY"] = "false"
    status_info = struct_to_table(get_complete_status_info())
    for _ in status_info:
        options.append(_[0])
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete
    )


def user_ids(ctx, param, incomplete):
    """Prepare a list of username for admin update/delete/password command."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []
    for _ in list_users():
        options.append(
            (
                _["username"]
            )
        )
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def user_group_ids(ctx: Context, param, incomplete):
    """Prepare a list of group name for admin user update
     --unassign-group/--assign-group parameter"""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    if not ctx.args:
        return []
    users = get_user_by_username(username=str(ctx.args[0]))
    if not users:
        return []

    if param.name == "unassign_group":
        groups = user_groups(user_id=users[0]["id"])
    else:
        user_group_names = (
            [group["name"] for group in user_groups(user_id=users[0]["id"])]
        )
        groups = (
            [group for group in list_groups() if group["name"] not in user_group_names]
        )
    options = []
    for _ in groups:
        options.append(
            (
                _["name"]
            )
        )

    for arg in ctx.params["assign_group"]:
        with suppress(ValueError):
            options.remove(arg)
    for arg in ctx.params["unassign_group"]:
        with suppress(ValueError):
            options.remove(arg)

    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def client_ids(ctx, param, incomplete):
    """Prepare a list of client ids for admin secret and update command."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []
    for _ in list_open_id_clients():
        options.append(
            (
                _["clientId"]
            )
        )
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def transformation_task_ids(ctx, param, incomplete):
    """Prepare a list of projectId:transformation task identifier."""
    CONTEXT.set_connection_from_params(ctx.find_root().params)
    options = []
    results = list_items(item_type="transform")
    datasets = results["results"]
    for _ in datasets:
        options.append(
            (
                _["projectId"] + ":" + _["id"],
                _["label"]
            )
        )
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )


def linking_task_ids(ctx, args, incomplete):
    """Prepare a list of projectId:linking task identifier."""
    CONTEXT.set_connection_from_args(args)
    options = []
    results = list_items(item_type="linking")
    datasets = results["results"]
    for _ in datasets:
        options.append(
            (
                _["projectId"] + r"\:" + _["id"],
                _["label"]
            )
        )
    return _finalize_completion(
        candidates=options,
        incomplete=incomplete,
        sort_by=SORT_BY_DESC
    )
