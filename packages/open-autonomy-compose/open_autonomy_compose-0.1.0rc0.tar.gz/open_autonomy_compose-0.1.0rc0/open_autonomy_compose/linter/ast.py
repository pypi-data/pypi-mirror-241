"""AST Helpers."""

import ast
import inspect
import re
import typing as t
from typing import Any


FIND_FROM_GET_NAME_RE = re.compile(r"get_name\([a-zA-Z]+\.([a-z0-9_]+)\)")
FIND_FROM_LITERAL_RE = re.compile(r"\'([a-zA-Z0-9_]+)\': ")
FIND_SNAKE_CASE_RE = re.compile(r"[a-zA-Z0-9_]+")

_parse_cache: t.Dict[str, t.Dict[str, t.Set[str]]] = {}


def _parse_call_for_updates(
    node: ast.Call, varibales: t.Dict[str, ast.AST]
) -> t.Set[str]:
    """Parse ast.Call for sync db updates."""
    updates: t.Set[str] = set()
    if not isinstance(node.func, ast.Attribute):
        return updates

    if node.func.attr != "update":
        return updates

    if not isinstance(node.func.value, ast.Attribute):
        return updates

    if node.func.value.attr != "synchronized_data":
        return updates

    for kwd in node.keywords:
        if kwd.arg is not None and kwd.arg != "synchronized_data_class":
            updates.add(kwd.arg)

    update_code = ast.unparse(node)
    updates.update(FIND_FROM_GET_NAME_RE.findall(update_code))
    updates.update(FIND_FROM_LITERAL_RE.findall(update_code))

    refs = re.findall(r"self\.([a-zA-Z0-9_]+): ", update_code)
    for ref in refs:
        assoc = varibales.get(ref)
        if assoc is None:
            continue
        assoc_code = ast.unparse(assoc)
        found = FIND_FROM_GET_NAME_RE.findall(assoc_code) + FIND_SNAKE_CASE_RE.findall(
            assoc_code
        )
        if len(found) == 0:
            continue
        updates.update(found)
    return updates


def _parse_assign_for_updates(
    node: ast.Assign, variables: t.Dict[str, ast.AST]
) -> t.Set[str]:
    """Parse ast.Assign for sync db updates."""
    updates: t.Set[str] = set()
    if not isinstance(node.value, ast.Call):
        return updates
    updates.update(_parse_call_for_updates(node=node.value, varibales=variables))
    return updates


def _parse_return_for_exit_events(
    node: ast.Return, variables: t.Dict[str, ast.AST]
) -> t.Tuple[t.Optional[str], t.Set[str]]:
    """Parse ast.Return for exit events."""

    updates: t.Set[str] = set()
    if not isinstance(node.value, ast.Tuple):
        return None, updates

    sync_db, exit_event = node.value.elts
    if isinstance(sync_db, ast.Call):
        updates.update(_parse_call_for_updates(sync_db, varibales=variables))

    if not isinstance(exit_event, ast.Attribute):
        return None, updates

    if t.cast(ast.Name, exit_event.value).id == "Event":
        return exit_event.attr, updates

    if t.cast(ast.Name, exit_event.value).id == "self":
        assoc_var = variables.get(exit_event.attr)
        if assoc_var is None:
            return None, updates
        return t.cast(ast.Attribute, assoc_var).attr, updates

    return None, updates
    # if isinstance(exit_event, ast.Subscript): # noqa: E800
    #     slice_val = exit_event.slice.attr # noqa: E800
    #     if isinstance(exit_event.value, ast.Attribute): # noqa: E800
    #         container_name = t.cast(ast.Attribute, exit_event.value).attr # noqa: E800
    #     else: # noqa: E800
    #         container_name = t.cast(ast.Name, exit_event.value).id # noqa: E800


def _parse_updates_recursively(
    body: t.Any,
    updates: t.Set[str],
    event_to_updates: t.Dict[str, t.Set[str]],
    variables: t.Dict,
) -> None:
    """Parse updates recursively."""
    if isinstance(body, list):
        for _node in body:
            _parse_updates_recursively(
                body=_node,
                updates=updates,
                event_to_updates=event_to_updates,
                variables=variables,
            )
        return

    if isinstance(body, ast.If):
        if any(map(lambda x: isinstance(x, ast.Return), body.body)):
            _updates = updates.copy()
        else:
            _updates = updates
        for _node in body.body:
            _parse_updates_recursively(
                body=_node,
                updates=_updates,
                event_to_updates=event_to_updates,
                variables=variables,
            )

        if any(map(lambda x: isinstance(x, ast.Return), body.orelse)):
            _updates = updates.copy()
        else:
            _updates = updates
        for _node in body.orelse:
            _parse_updates_recursively(
                body=_node,
                updates=_updates,
                event_to_updates=event_to_updates,
                variables=variables,
            )

    if isinstance(body, ast.Assign) and len(body.targets) == 1:
        updates.update(_parse_assign_for_updates(node=body, variables=variables))
        return

    if isinstance(body, ast.Return):
        exit_event, exit_updates = _parse_return_for_exit_events(
            node=body, variables=variables
        )
        if exit_event is None:
            return
        event_to_updates[exit_event] = {*updates, *exit_updates}


class RoundVisitor(ast.NodeVisitor):
    """Round visitor."""

    def __init__(self, variables: t.Dict[str, ast.AST]) -> None:
        """Initialize object."""
        self.event_to_updates: t.Dict[str, t.Set] = {}
        self.variables = variables

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        """Visit function def."""
        if node.name != "end_block":
            return

        updates: t.Set[str] = set()
        _parse_updates_recursively(
            body=node.body,
            updates=updates,
            event_to_updates=self.event_to_updates,
            variables=self.variables,
        )


class SelectionKeyStateVisitor(ast.NodeVisitor):
    """Visitor for state with selection_key defined."""

    def __init__(self) -> None:
        """Initialize object."""
        self.event_to_updates: t.Dict[str, t.Set] = {}

    def visit_Assign(self, node: ast.Assign) -> Any:
        """Visit assign operator."""
        if len(node.targets) != 1:
            return
        (target,) = node.targets
        if not isinstance(target, ast.Name):
            return
        if target.id == "selection_key":
            updates = set()
            nodestr = ast.unparse(node)
            updates.update(re.findall(r"get_name\([a-zA-Z]+\.([a-z0-9_]+)\)", nodestr))
            updates.update(re.findall(r"'([a-z0-9_]+)'", nodestr))
            self.event_to_updates["DONE"] = updates


class LocalVariablesVisitor(ast.NodeVisitor):
    """Parse local variables of a class."""

    def __init__(self) -> None:
        """Initialize object."""
        self.local_vars: t.Dict[str, ast.AST] = {}

    def visit_Assign(self, node: ast.Assign) -> Any:
        """Visit Assign"""
        target = node.targets[0]
        if isinstance(target, ast.Name):
            self.local_vars[target.id] = node.value


class DerivedClassVisitor(ast.NodeVisitor):
    """Derived class visitor."""

    def __init__(self) -> None:
        """Initialize object."""
        self.event_to_updates: t.Dict[str, t.Set[str]] = {}

    def visit_ClassDef(self, node: ast.ClassDef) -> Any:
        """Vist ClassDef"""
        for base in node.bases:
            self.event_to_updates.update(
                _parse_cache.get(t.cast(ast.Name, base).id, {})
            )


def parse_local_variables(node: ast.AST) -> t.Dict[str, ast.AST]:
    """Parse local variables of a node."""
    visitor = LocalVariablesVisitor()
    visitor.visit(node=node)
    return visitor.local_vars


def parse_updates(cls: t.Any) -> t.Dict[str, t.Set[str]]:
    """Parse exit event -> updates."""
    code = inspect.getsource(cls)
    node = ast.parse(code)

    if "end_block" in code:
        visitor = RoundVisitor(variables=parse_local_variables(node=node))  # type: ignore
    elif "selection_key" in code:
        visitor = SelectionKeyStateVisitor()  # type: ignore
    else:
        # TODO: This does not work
        visitor = DerivedClassVisitor()  # type: ignore
    visitor.visit(node=node)
    _parse_cache[cls.__name__] = visitor.event_to_updates
    return _parse_cache[cls.__name__]
