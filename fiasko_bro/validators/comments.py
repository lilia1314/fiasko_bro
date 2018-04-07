import ast

from .. import ast_helpers
from .. import url_helpers


def has_no_extra_dockstrings(solution_repo, whitelists, functions_with_docstrings_percent_limit, *args, **kwargs):
    whitelist = whitelists.get('has_no_extra_dockstrings_whitelist', [])
    for parsed_file in solution_repo.get_parsed_py_files(whitelist=whitelist):
        defs = ast_helpers.get_nodes_of_type(parsed_file.ast_tree, ast.FunctionDef)
        if not defs:
            continue

        docstrings = [ast.get_docstring(d) for d in defs if ast.get_docstring(d) is not None]
        if len(docstrings) / len(defs) * 100 > functions_with_docstrings_percent_limit:
            return 'extra_comments', parsed_file.name
