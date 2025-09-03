# pip3 install python-constraint//// do this to get constraint library ...!!
from constraint import Problem, AllDifferentConstraint

def map_coloring_problem():
    problem = Problem()

    # Define the variables and their possible values (colors)
    colors = ["Red", "Green", "Blue"]
    regions = ["A", "B", "C"]
   
    # Add variables
    problem.addVariables(regions, colors)

    # Define adjacency constraints
    problem.addConstraint(lambda a, b: a != b, ("A", "B"))
    problem.addConstraint(lambda a, b: a != b, ("B", "C"))

    # Ensure all regions have different colors
    problem.addConstraint(AllDifferentConstraint(), regions)

    # Solve the problem
    solutions = problem.getSolutions()

    return solutions

if __name__ == "__main__":
    solutions = map_coloring_problem()
    if solutions:
        for solution in solutions:
            print(solution)
    else:
        print("No solutions found.")