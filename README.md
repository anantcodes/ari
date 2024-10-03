# ari

## Brief 
This repository contains python codes for various algorithms.

## Details

## Constraint Satisfactory Problem 
A CSP involves a set of variables, each of which must be assigned a value from a specific domain, subject to certain constraints. The goal is to find an assignment of values to the variables that satisfies all the constraints.
### Key Components of CSPs:
Variables: These are the entities that need to be assigned values.
Domains: Each variable has a domain, which is a set of possible values it can take.
Constraints: These define the relationships between variables, specifying which combinations of values are permissible.
### Common Examples:
Sudoku: Each cell (variable) must be filled with a number (value) that satisfies constraints (no duplicate numbers in rows, columns, and boxes).
Map coloring: Assign colors to different regions (variables) such that no adjacent regions (constraints) share the same color.
### Approaches to Solve CSPs:
Backtracking: A depth-first search method that tries to build a solution incrementally, backtracking when a constraint is violated.
Constraint Propagation: Techniques like arc-consistency reduce the domains of variables before searching.
Heuristics: Strategies to decide the order of variable assignments (e.g., Minimum Remaining Values or Degree Heuristic).
