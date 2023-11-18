"""Check composition."""

from pathlib import Path

from autonomy.cli.helpers.analyse import load_package_tree
from clea import Directory, command
from typing_extensions import Annotated

from open_autonomy_compose.fsm.composition import Composition
from open_autonomy_compose.linter.db import check_db_conditions


@command
def check(
    app: Annotated[Path, Directory(exists=True, resolve=True)],
) -> None:
    """Perform composition checks."""
    load_package_tree(
        packages_dir=app.parent.parent.parent,
    )
    composition = Composition.from_path(
        path=app,
    )
    check_db_conditions(
        composition=composition,
    )
