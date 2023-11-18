"""FSM Composition helpers."""

import ast
import importlib
import inspect
import os
import re
import typing as t
from enum import Enum
from pathlib import Path
from types import ModuleType


class EventType(Enum):
    """Event type."""

    SENTINAL = "sentinal"
    DONE = "done"


StateType = t.Any
TransitionFunction = t.Dict[StateType, t.Dict[EventType, StateType]]


class AbciApp:
    """AbciApp abstraction"""

    initial_round_cls: StateType
    initial_states: t.Set[StateType] = set()
    transition_function: TransitionFunction
    final_states: t.Set[StateType] = set()
    event_to_timeout: t.Dict[StateType, float] = {}
    cross_period_persisted_keys: t.FrozenSet[str] = frozenset()
    background_round_cls: t.Optional[StateType] = None
    termination_transition_function: t.Optional[TransitionFunction] = None
    termination_event: t.Optional[StateType] = None
    default_db_preconditions: t.Set[str] = set()
    db_pre_conditions: t.Dict[StateType, t.Set[str]] = {}
    db_post_conditions: t.Dict[StateType, t.Set[str]] = {}


AbciAppType = t.Type[AbciApp]


class Composition:
    """Composition module representation."""

    def __init__(
        self,
        name: str,
        module: ModuleType,
        app: AbciAppType,
        events: EventType,
        is_chained: bool = False,
        abci_apps: t.Optional[t.Dict[str, AbciAppType]] = None,
    ) -> None:
        """Composition module."""
        self.name = name
        self.module = module
        self.app = app
        self.events = events
        self.is_chained = is_chained
        self.abci_apps = abci_apps or {}

    @staticmethod
    def find_fsm_app(module: ModuleType) -> t.Tuple[str, AbciAppType]:
        """Find FSM app class from a module."""
        for cls in dir(module):
            obj = getattr(module, cls)
            try:
                for base in obj.__bases__:
                    if base.__name__ == "AbciApp":
                        obj.__name__ = cls
                        return cls, obj
            except AttributeError:
                continue
        raise ValueError(
            f"Could not find FSM app class from the provided module: {module}"
        )

    @staticmethod
    def laod_module(path: Path, name: str) -> ModuleType:
        """Import and validate rounds.py module."""
        root_dir = os.path.abspath(os.curdir)
        if str(path).startswith(root_dir):
            path = path.relative_to(root_dir)
        import_name = ".".join((path / name).parts)
        return importlib.import_module(import_name)

    @classmethod
    def from_app(cls, module: ModuleType) -> "Composition":
        """Load from single app."""
        name, app = cls.find_fsm_app(module=module)
        return cls(
            name=name,
            app=app,
            module=module,
            events=getattr(module, "Event"),  # noqa: B009
            is_chained=False,
        )

    @staticmethod
    def get_event_enum(app: AbciAppType) -> EventType:
        """Return event enum."""
        events = {"SENTINAL": "sentinal"}
        for transition in app.transition_function.values():
            for event in transition.keys():
                events[event.name] = event.value
        return t.cast(EventType, Enum("Event", events))

    @classmethod
    def from_composition(cls, module: ModuleType) -> "Composition":
        """Load from single app."""
        name, app = cls.find_fsm_app(module=module)
        abci_apps = {}
        for node in ast.parse(inspect.getsource(module)).body:
            if (
                isinstance(node, ast.Assign)
                and isinstance(node.value, ast.Call)
                and node.value.func.id == "chain"  # type: ignore
            ):
                code = ast.unparse(node.value)
                for module_app in re.findall(r"[A-Z][a-zA-Z0-9]+\.[a-zA-Z0-9]+", code):
                    abci_module, abci_app = module_app.split(".")
                    abci_apps[abci_app] = getattr(
                        getattr(module, abci_module), abci_app
                    )
        return cls(
            name=name,
            app=app,
            module=module,
            events=cls.get_event_enum(app=app),
            is_chained=True,
            abci_apps=abci_apps,
        )

    @classmethod
    def from_path(cls, path: Path) -> "Composition":
        """Load from path."""
        module_name = "rounds"
        if not (path / "rounds.py").exists():
            if not (path / "composition.py").exists():
                raise FileNotFoundError(
                    f"Cannot find the rounds module or the composition module for {path}"
                )
            module_name = "composition"
        module = cls.laod_module(path=path, name=module_name)
        if module_name == "composition":
            return cls.from_composition(module=module)
        return cls.from_app(module=module)
