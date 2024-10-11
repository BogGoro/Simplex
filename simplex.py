from typing import List

def solve_with_simplex(num_constraints: int, c: List[float], A: List[List[float]], b: List[float], epsilon: float):
    if sum( x < 0 for x in b) > 0:
        print("The method is not applacable!")
        exit(0)

    num_vars = len(A[0])
    tableau = []

    # creating initial tableu by adding constraints with slack variables and RHS
    tableau = [
        row[:] + [0] * num_constraints + [b[i]]
        for i, row in enumerate(A)
        ]

    # Add the objective function row with slack variables and RHS
    tableau.insert(0, [-c[j] for j in range(num_vars)] + [0] * (num_constraints + 1))


    for i in range(1, num_constraints + 1):
        tableau[i][num_vars + i - 1] = 1  # Add Slack variable to constraint rows

    # Simplex iterations
    while True:
        # Check if the current solution is optimal
        if all(x >= -epsilon for x in tableau[0][:-1]):
            break

        # Choose the most negative coefficient in the objective row
        pivot_col = min(range(len(tableau[0]) - 1), key=lambda j: tableau[0][j])

        # If no positive entry in the pivot column, the problem is unbounded
        if all(row[pivot_col] <= epsilon for row in tableau[1:]):
            print("The method is not applacable!")
            exit(0)

        # Choose the leaving variable
        ratios = [
            (tableau[i][-1] / tableau[i][pivot_col], i)
            for i in range(1, num_constraints + 1) if tableau[i][pivot_col] > epsilon
            ]
        pivot_row = min(ratios)[1]

        # Perform the pivot
        pivot_value = tableau[pivot_row][pivot_col]
        tableau[pivot_row] = [x / pivot_value for x in tableau[pivot_row]]

        for i in range(len(tableau)):
            if i != pivot_row:
                row_factor = -tableau[i][pivot_col]
                tableau[i] = [tableau[i][j] + row_factor * tableau[pivot_row][j] for j in range(len(tableau[i]))]


    solution = [0] * num_vars
    for i in range(num_vars):
        if sum(-epsilon < tableau[j][i] < epsilon for j in range(len(tableau))) == num_constraints and \
            sum(1 - epsilon < tableau[j][i] < 1 + epsilon for j in range(len(tableau))) == 1:
            variable_row = sum(j if (1 - epsilon < tableau[j][i] < 1 + epsilon) else 0 for j in range(len(tableau)))
            solution[i] = tableau[variable_row][-1]

    optimal_value = tableau[0][-1]

    print(solution)
    print(optimal_value)
    


n = int(input()) # number of constraints
c = list(map(int, input().split()))
A = []
for i in range(n):
    constraint = list(map(int, input().split()))
    A.append(constraint)
b = list(map(int, input().split()))
epsilon = float(input())

solve_with_simplex(n, c, A, b, epsilon)