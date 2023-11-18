"""Transitions helpers."""

import typing as t

from open_autonomy_compose.fsm.composition import Composition, EventType, StateType


class Transitions:
    """Class to represent FSM transitions."""

    @classmethod
    def _build(
        cls,
        state: StateType,
        previous_state: StateType,
        transition_event: EventType,
        composition: Composition,
        local_transitions: t.Dict[StateType, t.Dict[str, StateType]],
        transitions: t.Dict,
        visited: t.List[StateType],
    ) -> None:
        """Build possible transition path tree."""
        if transition_event != composition.events.SENTINAL:
            local_state = local_transitions[previous_state][transition_event.name]
            if local_state.__name__.startswith("Finished"):
                transitions[previous_state] = {
                    transition_event.name: local_state,
                    **transitions.get(previous_state, {}),
                }
                transitions[local_state] = {
                    composition.events.DONE.name: state,
                    **transitions.get(local_state, {}),
                }
            else:
                transitions[previous_state] = {
                    transition_event.name: state,
                    **transitions.get(previous_state, {}),
                }

        for event, next_state in composition.app.transition_function[state].items():
            if next_state in visited:
                local_state = local_transitions[state][event.name]
                if local_state.__name__.startswith("Finished"):
                    transitions[state] = {
                        transition_event.name: local_state,
                        **transitions.get(state, {}),
                    }
                    transitions[local_state] = {
                        composition.events.DONE.name: next_state,
                        **transitions.get(local_state, {}),
                    }
                else:
                    transitions[state] = {
                        event.name: next_state,
                        **transitions.get(state, {}),
                    }
                continue
            visited.append(next_state)
            cls._build(
                state=next_state,
                previous_state=state,
                transition_event=event,
                composition=composition,
                local_transitions=local_transitions,
                transitions=transitions,
                visited=visited,
            )

    @staticmethod
    def _get_local_transitions(
        composition: Composition,
    ) -> t.Dict[StateType, t.Dict[str, StateType]]:
        """Get mapping of local transitions from AbciApp objects."""
        state_to_local_transitions = {}
        for abci_app in composition.abci_apps.values():
            for state, transitions in abci_app.transition_function.items():
                state_to_local_transitions[state] = {
                    event.name: next_state for event, next_state in transitions.items()
                }
        return state_to_local_transitions

    @classmethod
    def from_composition(
        cls,
        composition: Composition,
        start_state: StateType,
    ) -> t.Dict[StateType, t.Dict[str, StateType]]:
        """Build from Composition object."""

        local_transitions = cls._get_local_transitions(composition=composition)
        transitions: t.Dict[StateType, t.Dict[str, StateType]] = {}
        visited: t.List[StateType] = []
        cls._build(
            state=start_state,
            previous_state=start_state,
            transition_event=composition.events.SENTINAL,
            composition=composition,
            local_transitions=local_transitions,
            transitions=transitions,
            visited=visited,
        )
        return transitions
