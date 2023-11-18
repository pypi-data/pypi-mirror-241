"""Linters for SynchronizedDb"""


import typing as t
from enum import Enum

from open_autonomy_compose.fsm.composition import Composition, StateType
from open_autonomy_compose.fsm.transitions import Transitions
from open_autonomy_compose.linter.ast import parse_updates


def _check_conditions(
    current_state: StateType,
    previous_state: StateType,
    previous_updates: t.Set[str],
    transitions: t.Dict[StateType, t.Dict[Enum, StateType]],
    degenerate_state_to_post_conditions: t.Dict[StateType, t.Set[str]],
    verified: t.List[StateType],
) -> None:
    """Check conditions."""
    if current_state in degenerate_state_to_post_conditions:
        missing_updates = (
            degenerate_state_to_post_conditions[current_state] - previous_updates
        )
        if len(missing_updates) > 0:
            print(
                f"- ERROR: {current_state.__name__} requires following SynchronisedDB parameters but none of the "
                f"previous states performs this update: {missing_updates}; Previous state: {previous_state.__name__}"
            )

    if current_state not in transitions:
        return

    updates = parse_updates(current_state)
    for exit_event, next_state in transitions[current_state].items():
        _previous_updates = {*previous_updates, *updates.get(exit_event, set())}
        if next_state in verified:
            if next_state in degenerate_state_to_post_conditions:
                missing_updates = (
                    degenerate_state_to_post_conditions[next_state] - _previous_updates
                )
                if len(missing_updates) > 0:
                    print(
                        f"- WARNING: {next_state.__name__} requires following SynchronisedDB parameters but the none of the "
                        f" current previous states performs this update: {missing_updates}; Previous state: {current_state.__name__}"
                    )
            continue

        verified.append(next_state)
        _check_conditions(
            current_state=next_state,
            previous_state=current_state,
            previous_updates=_previous_updates,
            transitions=transitions,
            degenerate_state_to_post_conditions=degenerate_state_to_post_conditions,
            verified=verified,
        )
    return


def check_db_conditions(composition: Composition) -> None:
    """Check DB conditions."""
    transitions = Transitions.from_composition(
        composition=composition,
        start_state=composition.app.initial_round_cls,
    )
    degenerate_state_to_post_conditions = {}
    for abci_app in composition.abci_apps.values():
        for degenerate_state, conditions in abci_app.db_post_conditions.items():
            updates = degenerate_state_to_post_conditions.get(degenerate_state, set())
            updates.update(conditions)
            degenerate_state_to_post_conditions[degenerate_state] = updates

    verified = []
    _check_conditions(
        current_state=composition.app.initial_round_cls,
        previous_state=composition.app.initial_round_cls,
        previous_updates=set(),
        transitions=transitions,
        degenerate_state_to_post_conditions=degenerate_state_to_post_conditions,
        verified=verified,
    )
