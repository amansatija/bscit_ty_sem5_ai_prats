# pip3 install python-constraint//// do this to get constraint library ...!!
from constraint import Problem

# Create a new CSP problem
problem = Problem()

# Variables: regions of the map
variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Domain: colors available (Red, Green, Blue)
domain = ["Red", "Green", "Blue"]

# Add variables to the problem with their domain
problem.addVariables(variables, domain)

# Constraints: adjacent regions cannot have the same color
problem.addConstraint(lambda a, b: a != b, ("WA", "NT"))
problem.addConstraint(lambda a, b: a != b, ("WA", "SA"))
problem.addConstraint(lambda a, b: a != b, ("NT", "SA"))
problem.addConstraint(lambda a, b: a != b, ("NT", "Q"))
problem.addConstraint(lambda a, b: a != b, ("SA", "Q"))
problem.addConstraint(lambda a, b: a != b, ("SA", "NSW"))
problem.addConstraint(lambda a, b: a != b, ("SA", "V"))
problem.addConstraint(lambda a, b: a != b, ("Q", "NSW"))
problem.addConstraint(lambda a, b: a != b, ("NSW", "V"))

# Solve the problem
solutions = problem.getSolutions()

# Print the solutions
print(f"Number of solutions: {len(solutions)}")
for solution in solutions:
    print(solution)



# This script uses the constraint library to solve a classic map coloring problem. Here's a breakdown of how it works:

# Problem Definition:
# In 
# map_coloring_problem()
# , a Problem object is created. This object will hold all the variables, their possible values, and the rules they must follow.
# Variables and Domains:
# Variables: The regions ("A", "B", "C") are the variables in our problem. We need to assign a value to each of them.
# Domain: The colors ("Red", "Green", "Blue") are the domain, which is the set of possible values that can be assigned to each variable.
# problem.addVariables(regions, colors) tells the solver that each region can be assigned any of the specified colors.
# Constraints (The Rules):
# Constraints are the rules that a valid solution must obey.
# problem.addConstraint(lambda a, b: a != b, ("A", "B")) adds a rule that the color assigned to region "A" cannot be the same as the color for region "B".
# Similarly, problem.addConstraint(lambda a, b: a != b, ("B", "C")) ensures "B" and "C" have different colors.
# problem.addConstraint(AllDifferentConstraint(), regions) is a powerful global constraint. It enforces that all regions listed in regions must have a unique color.
# Solving:
# problem.getSolutions() is the core step. The library's solver uses algorithms (like backtracking search) to explore all possible color assignments. It systematically checks them against the constraints you've defined.
# It discards any assignment that violates even one constraint and keeps only the ones that satisfy all of them.
# Output:
# The script then prints each valid solution found. A solution is a dictionary where keys are the regions and values are their assigned colors, for example: {'A': 'Red', 'B': 'Green', 'C': 'Blue'}.
# In short, the code translates the map coloring puzzle into a formal model that the constraint library can understand and solve systematically.


# Of course. Let's break down that line: problem.addConstraint(lambda a, b: a != b, ("A", "B")).

# This line adds a rule to your constraint satisfaction problem. It consists of two main parts:

# The Constraint Function: lambda a, b: a != b
# lambda: This keyword creates a small, one-line, anonymous function. Think of it as a quick way to define a function without giving it a name using def.
# a, b: These are the parameters of the lambda function. When the solver checks this constraint, a will hold the value (color) assigned to the first variable in the list, and b will hold the value for the second.
# a != b: This is the logic of the function. It's a simple comparison that returns True if the values of a and b are different, and False if they are the same.
# The Variables: ("A", "B")
# This tuple tells the solver which variables this constraint applies to. In this case, it's the regions "A" and "B".
# How It Works
# Together, problem.addConstraint(lambda a, b: a != b, ("A", "B")) tells the solver:

# "When you are trying to find a solution, the value (color) assigned to region "A" must not be equal to the value assigned to region "B". If they are the same, that's not a valid solution, so discard it and try something else."

# The solver will then use this rule, along with all the others you define, to find only the combinations of colors that satisfy every single constraint.