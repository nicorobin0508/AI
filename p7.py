from simpleai.search import CspProblem,backtrack

#STEP 1 : Define the variables
variables=('A','B','C','D')

#STEP 2 : Define the domains for each variable
domains={
    'A' : ['Red','Green','Blue'],
    'B' : ['Red','Green','Blue'],
    'C' : ['Red','Green','Blue'],
    'D' : ['Red','Green','Blue'],
    }

#STEP 3 : Define the constraint function    
def different_colors(variables,values):
    return values[0] != values[1]

#STEP 4 : Define the contraints
constraints=[
    (('A','B'),different_colors),
    (('A','C'),different_colors),
    (('A','D'),different_colors),
    (('B','C'),different_colors),
    (('C','D'),different_colors),
    ]

#STEP 5 : Create the CSP problem
problem=CspProblem(variables,domains,constraints)

#STEP 6 : Solve the problem using backtracking
solution=backtrack(problem)

#STEP 7 : Print the solution
print("Solution:")
print(solution)
