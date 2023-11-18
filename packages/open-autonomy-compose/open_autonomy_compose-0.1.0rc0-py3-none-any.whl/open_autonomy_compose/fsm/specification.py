"""FSM Specification helpers."""

import typing as t
from collections import OrderedDict
from pathlib import Path

from aea.helpers.yaml_utils import yaml_dump

from open_autonomy_compose.fsm.composition import Composition, EventType, StateType


def _find_parent(state: StateType) -> str:
    """Find parent name to a state class.."""
    # packages, author, skill, package_name, ...
    _, _, _, parent, *_ = state.__module__.split(".")
    return parent


def _to_name(state: StateType, include_parent: bool = False) -> str:
    """State class to name."""
    name = state.__name__
    if include_parent:
        name = f"{_find_parent(state=state)}.{name}"
    return name


class NamedState:
    """Named state object."""

    def __init__(
        self,
        state: StateType,
        name: str,
        parent: str,
    ) -> None:
        """Initialize object."""
        self.state = state
        self.parent = parent
        self._name = name

    @classmethod
    def from_cls(cls, state: StateType) -> "NamedState":
        """Parse from rounf object."""
        return cls(
            state=state,
            name=_to_name(state=state),
            parent=_find_parent(state=state),
        )

    def name(self, parent: bool = False) -> str:
        """State name with parent."""
        if parent:
            return f"{self.parent}.{self._name}"
        return self._name


class Transitions:
    """Transitions."""

    def __init__(
        self,
        transitions: t.OrderedDict[NamedState, t.OrderedDict[str, NamedState]],
    ) -> None:
        """Initialize object."""
        self.transitions = transitions

    @classmethod
    def from_function(
        cls,
        function: t.OrderedDict[StateType, t.OrderedDict[EventType, StateType]],
    ) -> "Transitions":
        """Parse from function."""
        transitions: t.OrderedDict[
            NamedState, t.OrderedDict[str, NamedState]
        ] = OrderedDict()
        for state, next_states in function.items():
            ns = NamedState.from_cls(state=state)
            transitions[ns] = OrderedDict()
            for event, next_state in next_states.items():
                transitions[ns][event.name] = NamedState.from_cls(state=next_state)
        return cls(
            transitions=transitions,
        )

    def to_json(
        self, include_parent: bool = False
    ) -> t.OrderedDict[str, t.OrderedDict[str, str]]:
        """To json object."""
        transitions: t.OrderedDict[str, t.OrderedDict[str, str]] = OrderedDict()
        for state, next_states in self.transitions.items():
            name = state.name(parent=include_parent)
            transitions[name] = OrderedDict()
            for event, next_state in next_states.items():
                transitions[name][event] = next_state.name(parent=include_parent)
        return transitions

    def __repr__(self) -> str:
        """String representation."""
        s = ""
        for state, exits in self.transitions.items():
            s += f"{state}:\n"
            for event, next_event in exits.items():
                s += f"    {event}: {next_event}\n"
        s = s[:-1]
        return s


class FSMSpecification:
    """FSM Specification representation."""

    def __init__(
        self,
        name: NamedState,
        events: t.List[NamedState],
        start_state: NamedState,
        initial_states: t.List[NamedState],
        final_states: t.List[NamedState],
        transitions: Transitions,
    ) -> None:
        """Initialize object."""
        self.name = name
        self.events = events
        self.start_state = start_state
        self.initial_states = initial_states
        self.final_states = final_states
        self.transitions = transitions

    def to_json(self, include_parent: bool = False) -> t.OrderedDict:
        """To JSON object."""
        return OrderedDict(
            name=self.name.name(parent=include_parent),
            events=self.events,
            start_state=self.start_state.name(parent=include_parent),
            initial_states=list(
                map(lambda x: x.name(parent=include_parent), self.initial_states)
            ),
            final_states=list(
                map(lambda x: x.name(parent=include_parent), self.final_states)
            ),
            transitions=self.transitions.to_json(include_parent=include_parent),
        )

    def to_yaml(self, file: Path, include_parent: bool = False) -> None:
        """Dump to YAML file."""
        with file.open("w+") as fp:
            yaml_dump(self.to_json(include_parent=include_parent), fp)

    @classmethod
    def from_yaml(cls, file: Path) -> "FSMSpecification":
        """Load from a YAML file."""
        return NotImplemented

    @classmethod
    def from_compostion(cls, composition: Composition) -> "FSMSpecification":
        """Load from compostion."""
        _, _, _, skill_name, *_ = composition.module.__name__.split(".")
        return cls(
            name=NamedState(
                state=composition.app, name=composition.name, parent=skill_name
            ),
            events=[event.name for event in composition.events],
            start_state=NamedState.from_cls(composition.app.initial_round_cls),
            initial_states=[
                NamedState.from_cls(state)
                for state in getattr(composition.app, "initial_states", [])
            ],
            final_states=[
                NamedState.from_cls(state)
                for state in getattr(composition.app, "final_states", [])
            ],
            transitions=Transitions.from_function(
                function=composition.app.transition_function,
            ),
        )

    def __repr__(self) -> str:
        """String representation."""
        return f"<FSMSpecification name={self.name.name()}>"
