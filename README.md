# Laboratory Work 1

## Regular Grammar & Finite Automaton — Variant 26

**Course:** Formal Languages & Finite Automata  
**Author:** Bianca Tataroi  

---

## Theory

A formal language can be described using grammars and automata. A regular grammar is a type of grammar in which production rules follow a restricted form that allows the language to be recognized by a finite automaton. In this laboratory work, a right-linear grammar is analyzed. Right-linear grammars generate regular languages, which means they can be represented by finite automata.

There exists a fundamental equivalence between these two models. Every right-linear grammar can be transformed into a finite automaton, and every finite automaton recognizes a regular language. This project demonstrates that equivalence both theoretically and through a working implementation.

---

## Objectives

The objective of this work is to represent a regular grammar programmatically, to generate valid strings using the grammar, to convert the grammar into an equivalent finite automaton, and to verify whether given strings belong to the language using the automaton. Another important goal is to demonstrate the equivalence between grammars and automata in practice.

---

## Implementation Description

A class was created to represent the grammar by storing its nonterminals, terminals, start symbol, and production rules corresponding to Variant 26. The program generates valid strings by starting from the start symbol and repeatedly applying production rules until only terminal symbols remain. Because the grammar contains cycles, a maximum number of steps is used to prevent infinite derivations.

Since the grammar is right-linear, it can be converted directly into a finite automaton. Each nonterminal becomes a state, while productions that end with a terminal lead to a newly introduced final state. Another class implements the finite automaton and simulates its operation by processing input strings symbol by symbol and updating the current states according to the transition function. If a final state is reached after processing the entire string, the string is accepted as part of the language.

The main program constructs the grammar, converts it into the finite automaton, generates example strings, and tests multiple inputs for membership in the language.

---

## Program Structure

The implementation of the project is divided into three main modules: grammar.py, finite_automaton.py, and main.py. Each module is responsible for a specific part of the system and together they demonstrate the relationship between regular grammars and finite automata.

The grammar module defines the structure of the regular grammar and implements functions that generate valid strings using the production rules. The finite automaton module defines the automaton and provides functionality for verifying whether a given string belongs to the language. Finally, the main module coordinates the entire execution by creating the grammar, generating example strings, converting the grammar into an automaton, and testing strings for membership in the language.

---

## Grammar Class
The Grammar class represents a regular grammar by storing its fundamental components: the set of nonterminal symbols, the set of terminal symbols, the start symbol, and the production rules. The grammar implemented in this project corresponds to Variant 26 and contains the following production rules:

S → dA
A → aB | b
B → bC | d
C → cB | aA

These rules describe how valid strings of the language can be generated starting from the start symbol S.

 ### generate_string()

 The generate_string() function generates a valid string from the grammar. The process begins with the start symbol S and repeatedly applies production rules until only terminal symbols remain.

At each step the program checks which production rules are available for the current nonterminal and randomly selects one using the function random.choice(). This randomness allows the grammar to generate different valid strings every time the program is executed. To prevent infinite derivations caused by cycles in the grammar, a maximum number of derivation steps is imposed.

### generate_5_strings()

The generate_5_strings() function repeatedly calls the generate_string() function until five unique strings are generated. These strings serve as examples of valid words belonging to the language defined by the grammar.

### to_finite_automaton()

The to_finite_automaton() function converts the grammar into an equivalent finite automaton. Since the grammar is right-linear, the conversion can be performed directly. Each nonterminal symbol becomes a state in the automaton, and each production rule is transformed into a transition.

For example, a rule of the form

A → aB

is converted into the transition

A --a--> B

If a production ends with a terminal symbol, the transition leads to a newly introduced final state.

---

## Finite Automaton Class

The FiniteAutomaton class represents the automaton that recognizes the language generated by the grammar. It stores the following components:

- the set of states

- the input alphabet

- the transition function

- the start state

- the set of final states

### string_belongs_to_language()

The string_belongs_to_language() function checks whether a given input string belongs to the language recognized by the automaton.

The automaton starts in the start state and reads the input string symbol by symbol. For each symbol it follows the corresponding transition defined in the transition function. After processing the entire string, the automaton checks whether the current state belongs to the set of final states. If a final state is reached, the string is accepted; otherwise, it is rejected.

---

## Main Program

The main.py file controls the execution of the program. First, the grammar corresponding to Variant 26 is created. The program then generates several example strings using the grammar. Afterward, the grammar is converted into an equivalent finite automaton.

Finally, both the generated strings and additional test strings are verified using the automaton to determine whether they belong to the language. This process demonstrates that the automaton recognizes exactly the same language generated by the grammar.

## Conclusions

The implementation successfully generates valid strings from the grammar and verifies them using the finite automaton. All generated valid strings begin with the symbol d because of the production rule S → dA, and valid strings terminate with either b or d due to terminal productions. The presence of cycles in the grammar allows the creation of strings of arbitrary length. Strings that do not follow these rules are correctly rejected by the automaton.

The results confirm that the constructed automaton recognizes exactly the same language that is generated by the grammar. Therefore, the laboratory work demonstrates the theoretical principle that right-linear grammars and finite automata describe the same class of languages, namely regular languages.

## References

Course materials for Formal Languages & Finite Automata and lecture notes on regular grammars and finite automata were used as the primary sources of information.
