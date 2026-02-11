from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple
import random
from finite_automaton import FiniteAutomaton

# A production will be stored as:
# (terminal, next_nonterminal_or_empty)
Production = Tuple[str, str]


@dataclass
class Grammar:
    # Grammar = {Vn, Vt, P, S}
    vn: List[str]                          # nonterminals
    vt: List[str]                          # terminals
    start_symbol: str                      # S
    productions: Dict[str, List[Production]]  # P

    @staticmethod
    def variant_26() -> "Grammar":
        vn = ["S", "A", "B", "C"]
        vt = ["a", "b", "c", "d"]
        start = "S"

        productions = {
            "S": [("d", "A")],
            "A": [("a", "B"), ("b", "")],
            "B": [("b", "C"), ("d", "")],
            "C": [("c", "B"), ("a", "A")],
        }
        return Grammar(vn=vn, vt=vt, start_symbol=start, productions=productions)

    def generate_string(self, max_steps: int = 40) -> str:
        """
        Generate ONE valid string from the grammar by doing derivations.
        max_steps avoids infinite loops because there are cycles (A<->B<->C).
        """
        sentential = [self.start_symbol]  # start from S

        for _ in range(max_steps):
            # find the first nonterminal in the current sentential form
            idx = None
            for i, sym in enumerate(sentential):
                if sym in self.vn:
                    idx = i
                    break

            # if no nonterminals, we're done (only terminals left)
            if idx is None:
                return "".join(sentential)

            nt = sentential[idx]  # the nonterminal to expand (S/A/B/C)
            options = self.productions.get(nt, [])
            if not options:
                raise RuntimeError(f"No productions for nonterminal {nt}")

            terminal, next_nt = random.choice(options)

            # Replace nt with terminal (+ next nonterminal if exists)
            if next_nt == "":
                sentential[idx:idx+1] = [terminal]
            else:
                sentential[idx:idx+1] = [terminal, next_nt]

        raise RuntimeError("Generation hit max_steps (cycle). Try again or increase max_steps.")

    def generate_5_strings(self) -> List[str]:
        """
        Generate 5 (preferably unique) valid strings.
        Retries if generation loops.
        """
        result: List[str] = []
        attempts = 0

        while len(result) < 5 and attempts < 200:
            attempts += 1
            try:
                w = self.generate_string()
                if w not in result:
                    result.append(w)
            except RuntimeError:
                # looped; retry
                continue

        if len(result) < 5:
            raise RuntimeError("Could not generate 5 strings. Increase attempts/max_steps.")

        return result

    def to_finite_automaton(self) -> FiniteAutomaton:
        FINAL = "F"

        states = set(self.vn)
        states.add(FINAL)

        alphabet = set(self.vt)

        delta: Dict[tuple[str, str], set[str]] = {}

        def add_transition(from_state: str, symbol: str, to_state: str):
            key = (from_state, symbol)
            if key not in delta:
                delta[key] = set()
            delta[key].add(to_state)

        for left, productions in self.productions.items():
            for terminal, next_nt in productions:
                if next_nt == "":
                    add_transition(left, terminal, FINAL)
                else:
                    add_transition(left, terminal, next_nt)

        frozen_delta = {k: frozenset(v) for k, v in delta.items()}

        return FiniteAutomaton(
            states=frozenset(states),
            alphabet=frozenset(alphabet),
            delta=frozen_delta,
            start_state=self.start_symbol,
            final_states=frozenset({FINAL}),
        )
