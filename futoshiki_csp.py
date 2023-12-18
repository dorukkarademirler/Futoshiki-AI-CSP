#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects 
representing the board. The returned list of lists is used to access the 
solution. 

For example, after these three lines of code

    csp, var_array = futoshiki_csp_model_1(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array[0][0].get_assigned_value() should be the correct value in the top left
cell of the Futoshiki puzzle.

1. futoshiki_csp_model_1 (worth 20/100 marks)
    - A model of a Futoshiki grid built using only 
      binary not-equal constraints for both the row and column constraints.

2. futoshiki_csp_model_2 (worth 20/100 marks)
    - A model of a Futoshiki grid built using only n-ary 
      all-different constraints for both the row and column constraints. 

'''
from cspbase import *
import itertools


from cspbase import *


def futoshiki_csp_model_1(futo_grid):
    size = len(futo_grid)
    domain = list(range(1, size + 1))

    X = []
    for i, row in enumerate(futo_grid):
        for j, elem in enumerate(row):
            if isinstance(elem, int):
                if elem:
                    variable = Variable(f"({i},{j//2})", [elem])
                else:
                    variable = Variable(f"({i},{j//2})", domain)
                X.append(variable)

    # Equality Constraints
    constraint_list = []
    for i in range(size):
        for j in range(size):
            var1 = X[i * size + j]
            # Row
            for col in range(size):
                if col != j:
                    var2 = X[i * size + col]
                    constraint = Constraint(f"({var1} != {var2})", [var1, var2])
                    constraint.add_satisfying_tuples([(x, y) for x, y in itertools.product(var1.cur_domain(), var2.cur_domain()) if x != y])
                    constraint_list.append(constraint)

            # Column
            for row in range(size):
                if row != i:
                    var2 = X[row * size + j]
                    constraint = Constraint(f"({var1} != {var2})", [var1, var2])
                    constraint.add_satisfying_tuples([(x, y) for x, y in itertools.product(var1.cur_domain(), var2.cur_domain()) if x != y])
                    constraint_list.append(constraint)

    # Inequality constraints
    for i, row in enumerate(futo_grid):
        for j, elem in enumerate(row):
            if elem == ">":
                left, right = j - 1, j + 1
            elif elem == "<":
                left, right = j + 1, j - 1
            else:
                continue
            var1 = X[(i * size) + left // 2]
            var2 = X[(i * size) + right // 2]
            constraint = Constraint(f"({var1} > {var2})", [var1, var2])
            constraint.add_satisfying_tuples([(x, y) for x, y in itertools.product(var1.cur_domain(), var2.cur_domain()) if x > y])
            constraint_list.append(constraint)

    X_matrix = [[X[i * size + j] for j in range(size)] for i in range(size)]

    csp = CSP("Futoshiki_Model_1", X)
    for constraint in constraint_list:
        csp.add_constraint(constraint)
    return csp, X_matrix


def futoshiki_csp_model_2(futo_grid):
    size = len(futo_grid)
    domain = list(range(1, size + 1))

    X = []
    for i, row in enumerate(futo_grid):
        for j, elem in enumerate(row):
            if isinstance(elem, int):
                if elem:
                    variable = Variable(f"({i},{j//2})", [elem])
                else:
                    variable = Variable(f"({i},{j//2})", domain)
                X.append(variable)

    # N-ary
    row_constraint_list = []
    col_constraint_list = []

    # Row
    for i in range(size):
        row_vars = []
        for j in range(size):
            row_vars.append(X[i * size + j])
        constraint_row = Constraint(f"diffRow{i}", row_vars)
        constraint_row.add_satisfying_tuples(itertools.permutations(domain, size))
        row_constraint_list.append(constraint_row)

    # Column
    for j in range(size):
        col_vars = []
        for i in range(size):
            col_vars.append(X[i * size + j])
        constraint_col = Constraint(f"diffCol{j}", col_vars)
        constraint_col.add_satisfying_tuples(itertools.permutations(domain, size))
        col_constraint_list.append(constraint_col)

    # Inequality constraints
    inequality_constraint_list = []
    for i, row in enumerate(futo_grid):
        for j, elem in enumerate(row):
            if elem == ">":
                left, right = j - 1, j + 1
            elif elem == "<":
                left, right = j + 1, j - 1
            else:
                continue
            var1 = X[(i * size) + left // 2]
            var2 = X[(i * size) + right // 2]
            constraint = Constraint("Inequality{}".format(len(inequality_constraint_list) + 1), [var1, var2])
            constraint.add_satisfying_tuples(
                [(x, y) for x, y in itertools.product(var1.cur_domain(), var2.cur_domain()) if x > y])
            inequality_constraint_list.append(constraint)

    all_constraints = row_constraint_list + col_constraint_list + inequality_constraint_list

    # CSP
    csp = CSP("Futoshiki_Model_2", X)
    for constraint in all_constraints:
        csp.add_constraint(constraint)

    X_matrix = [[X[i * size + j] for j in range(size)] for i in range(size)]

    return csp, X_matrix