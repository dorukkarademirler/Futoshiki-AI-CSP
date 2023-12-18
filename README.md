# Constraint Propagators and Futoshiki CSP Models

## Overview

This repository contains Python implementations for two constraint propagators – a Forward Checking constraint propagator and a Generalized Arc Consistence (GAC) constraint propagator. Additionally, it includes two different CSP encodings to solve the logic puzzle Futoshiki. The assignment is divided into two main parts, each addressing specific aspects of constraint satisfaction problems.


## Constraint Propagators

### Forward Checking (prop_FC)
A propagator function that utilizes the Forward Checking (FC) algorithm to check constraints that have exactly one uninstantiated variable in their scope. Prunes the domain appropriately. If `newVar` is `None`, forward checks all constraints. Else, if `newVar=var`, only check constraints containing `newVar`.

### Generalized Arc Consistence (prop_GAC)
A propagator function that propagates according to the Generalized Arc Consistency (GAC) algorithm. If `newVar` is `None`, runs GAC on all constraints. Else, if `newVar=var`, only check constraints containing `newVar`.

### Minimum Remaining Values Heuristic (ord_mrv)
A variable ordering heuristic that chooses the next variable to be assigned according to the Minimum Remaining Values (MRV) heuristic. Returns the variable with the most constrained current domain (i.e., the variable with the fewest legal values).



## Futoshiki CSP Models

### Model 1 (futoshiki_csp_model_1)
A CSP model built using only binary not-equal constraints for the row and column constraints, and binary inequality constraints.

### Model 2 (futoshiki_csp_model_2)
A CSP model built using n-ary all-different constraints for the row and column constraints, and binary inequality constraints.

## How to Run

To run the implementations, follow these steps:

1. Download the provided starter code.
2. Execute the respective Python scripts for the constraint propagators (`propagators.py`) and Futoshiki CSP models (`futoshiki_csp.py`).

## Important Notes

- The Futoshiki CSP models can be space-expensive, especially for constraints over many variables.
- Be mindful of the time complexity for identifying satisfying tuples, especially in the second Futoshiki CSP model.
