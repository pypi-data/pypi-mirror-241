"""CLI Module."""

import typing as t

from clea import group, run

from open_autonomy_compose.cli.check import check
from open_autonomy_compose.cli.fsm import fsm
from open_autonomy_compose.cli.inspect import inspect


@group
def compose() -> None:
    """Composer - A CLI tool for working with FSM applications."""


def main(argv: t.Optional[t.List[str]] = None) -> None:
    """Run compose CLI module."""
    run(
        cli=compose,
        argv=argv,
        isolated=False,
    )


compose.add_child(fsm)
compose.add_child(inspect)
compose.add_child(check)

if __name__ == "__main__":
    main()
