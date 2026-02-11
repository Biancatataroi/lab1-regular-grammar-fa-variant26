from grammar import Grammar


def print_finite_automaton(fa):
    print("\n===== FINITE AUTOMATON =====")
    print("States (Q):", sorted(fa.states))
    print("Alphabet (Σ):", sorted(fa.alphabet))
    print("Start state (q0):", fa.start_state)
    print("Final states (F):", sorted(fa.final_states))

    print("\nTransitions (δ):")
    for (state, symbol), next_states in sorted(fa.delta.items()):
        for ns in sorted(next_states):
            print(f"  δ({state}, {symbol}) → {ns}")


def main():
    g = Grammar.variant_26()

    print(" 5 generated strings")
    words = g.generate_5_strings()
    for w in words:
        print(" ", w)

    fa = g.to_finite_automaton()

    print_finite_automaton(fa)

    print("\nMembership check (should be True)")
    for w in words:
        print(f"  {w} -> {fa.string_belongs_to_language(w)}")

    print("\n Additional Tests")
    tests = ["d", "dab", "dd"]
    for t in tests:
        print(f"  {t} -> {fa.string_belongs_to_language(t)}")


if __name__ == "__main__":
    main()
