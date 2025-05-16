# Polynomial

## P vs NP

- Class P consists of problems that can be solved in polynomial time, i.e. an algorithm exists that runs in time O(n\*k), some constant k, where n is the size of the input
- Examples of Class P
  1. Sorting a list
  2. Binary Search
  3. Shortest Path Finding
  4. Matrix Multiplication
  5. Spell Check
- Class P problems are always effectively solvable
- Class NP; Efficiently verifiable problem, NP stands for non deterministic polynomial time
  - for each NP problem, there has to be a verifier algorithm in place.
  - Examples for NP:
  1. Input: A completed 9x9 sudoko grid
  2. Task: Check whether it satisifies the sudoku rules (unique values per row, colums and 3x3 block)
  3. Polynomial time verification involves scanning each row, column, and subgrid.

## NP Complete vs NP Hard

- A decision problem is NO compelete if:
  - It belongs to the class NP, i.e. a solution can be verified in polynomial time
  - Every other problem in NP can be reduced to a polynomial time.
  - P = NP
  - Examples:
    1. 3-SAT (Boolean Satisfiability)
    2. Subset sum problem
    3. Vertex Cover
    4. TSP

## Intractable Problems

- Brute Force Search
- Backtracking
- Greedy Algorithms
- Approximation algorithms
- Heuristics
