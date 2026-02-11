from dataclasses import dataclass
from typing import Dict, FrozenSet


@dataclass(frozen=True)
class FiniteAutomaton:
    states: FrozenSet[str]
    alphabet: FrozenSet[str]
    delta: Dict[tuple[str, str], FrozenSet[str]]
    start_state: str
    final_states: FrozenSet[str]

    def string_belongs_to_language(self, input_string: str) -> bool:
        current_states = {self.start_state}

        for symbol in input_string:
            if symbol not in self.alphabet:
                return False

            next_states = set()

            for state in current_states:
                transitions = self.delta.get((state, symbol), frozenset())
                next_states |= set(transitions)

            current_states = next_states

            if not current_states:
                return False

        return any(state in self.final_states for state in current_states)
