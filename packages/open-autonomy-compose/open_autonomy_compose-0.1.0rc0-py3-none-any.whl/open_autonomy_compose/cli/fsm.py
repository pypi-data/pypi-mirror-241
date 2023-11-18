"""FSM Helpers."""

import json
from enum import Enum
from pathlib import Path

from autonomy.cli.helpers.analyse import load_package_tree
from clea import ChoiceByFlag, Directory, File, group
from typing_extensions import Annotated

from open_autonomy_compose.fsm.composition import Composition
from open_autonomy_compose.fsm.specification import FSMSpecification


DEFAULT_OUTPUT_FILE = Path("./fsm.yaml")


class OutputType(Enum):
    """Output types."""

    JSON = "json"
    YAML = "yaml"


@group
def fsm() -> None:
    """FSM Helpers."""


@fsm.command(name="from-app")
def _from_app(
    app: Annotated[Path, Directory(exists=True, resolve=True)],
    output_type: Annotated[
        OutputType,
        ChoiceByFlag(
            enum=OutputType, default=OutputType.YAML, help="File output type."
        ),
    ],
    output: Annotated[Path, File(help="Path to output file.")] = DEFAULT_OUTPUT_FILE,
) -> None:
    """Generate specification from an ABCI app."""
    load_package_tree(packages_dir=app.parent.parent.parent)
    spec = FSMSpecification.from_compostion(
        composition=Composition.from_path(
            path=app,
        ),
    )
    if output_type == OutputType.YAML:
        spec.to_yaml(file=output, include_parent=True)
    else:
        data = spec.to_json(include_parent=True)
        with output.open("w+") as fp:
            json.dump(data, fp=fp, indent=2)
