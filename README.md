# Laboratory Work 1  
## Regular Grammar & Finite Automaton  
**Course:** Formal Languages & Finite Automata  
**Variant:** 26  
**Student:** Bianca Tataroi  
**Deadline:** 12 February 2026  

---

# 1. Introduction

This project implements a regular grammar (Variant 26) and demonstrates its equivalence to a finite automaton.

The implementation includes:

- Representation of the grammar structure
- Generation of valid strings from the grammar
- Conversion of the grammar into a finite automaton
- Verification of string membership using the automaton

This laboratory work demonstrates the theoretical equivalence between **right-linear grammars** and **finite automata**, both of which define regular languages.

---

# 2. Grammar Definition (Variant 26)

The grammar is defined as:

\[
G = (V_N, V_T, P, S)
\]

## Nonterminals
V_N = {S, A, B, C}

## Terminals
V_T = {a, b, c, d}

## Start Symbol
S

## Productions
S → dA
A → aB | b
B → bC | d
C → cB | aA


---

# 3. Type of Grammar

All productions are of the form:
X → tY
X → t

where:
- `X, Y ∈ V_N`
- `t ∈ V_T`

Therefore, the grammar is a **right-linear grammar**.

Since right-linear grammars generate regular languages, the language defined by Variant 26 is **regular**.

---

# 4. Language Characteristics

From the grammar structure, we can observe:

- Every valid string starts with `d` (because `S → dA`).
- A word can terminate only through:
  - `A → b`
  - `B → d`
- Therefore, every valid string ends with either `b` or `d`.
- The grammar contains cycles:
  - `A → aB`
  - `B → bC`
  - `C → aA`
  - `C → cB`

These cycles allow the generation of strings of arbitrary length.

---

# 5. Finite Automaton Construction

Since the grammar is right-linear, it can be converted into a finite automaton.

The resulting finite automaton is:

\[
FA = (Q, Σ, δ, q_0, F)
\]

## States
Q = {S, A, B, C, F}

A new final state `F` is introduced.

## Alphabet
Σ = {a, b, c, d}


## Start State
q0 = S


## Final States
F = {F}

## Transition Function (δ)

Derived directly from productions:

δ(S, d) → A
δ(A, a) → B
δ(A, b) → F
δ(B, b) → C
δ(B, d) → F
δ(C, c) → B
δ(C, a) → A


---

# 6. Implementation Overview

## 6.1 Grammar Class

The `Grammar` class stores:

- Nonterminals
- Terminals
- Start symbol
- Production rules

It provides:

- `generate_string()` – generates one valid word via derivation
- `generate_5_strings()` – generates five valid words
- `to_finite_automaton()` – converts the grammar into a finite automaton

---

## 6.2 String Generation

The algorithm:

1. Start from the sentential form `[S]`
2. Repeatedly:
   - Locate the first nonterminal
   - Replace it using one of its productions
3. Stop when only terminals remain

A `max_steps` limit prevents infinite loops due to grammar cycles.

---

## 6.3 Finite Automaton Class

The `FiniteAutomaton` class stores:

- States
- Alphabet
- Transition function
- Start state
- Final states

It provides:

- `string_belongs_to_language(input_string)`

This method simulates an NFA using a set of current states.

---

# 7. Program Execution

## Project Structure

lab1-regular-grammar-fa-variant26/
│
├── src/
│ ├── main.py
│ ├── grammar.py
│ └── finite_automaton.py
│
├── README.md
└── REPORT.md


## Run Instructions

From the project root directory:

```bash
python3 src/main.py
 
8. Example Output

Example generated strings:

db
dabcd
dad
dabcbcd
dabaad

Finite automaton transitions:

δ(A, a) → B
δ(A, b) → F
δ(B, b) → C
δ(B, d) → F
δ(C, a) → A
δ(C, c) → B
δ(S, d) → A


Membership results:

db -> True
dabcd -> True
dad -> True
d -> False
dab -> False
dd -> False
dac -> False

9. Theoretical Conclusion

This project demonstrates the fundamental result:

Every right-linear grammar defines a regular language.
Every regular language can be recognized by a finite automaton.

The implementation verifies this equivalence computationally by:

Generating strings from the grammar (generative perspective)

Recognizing strings using a finite automaton (recognition perspective)

Both approaches produce consistent results.

10. Final Remarks

This laboratory work successfully:

Models a formal grammar in code

Generates valid language strings

Converts the grammar into a finite automaton

Verifies language membership

Demonstrates the equivalence between regular grammars and finite automata

The implementation is modular, documented, and fully executable.

