from simpleai.search import SearchProblem, astar

GOAL = 'HELLO WORLD'

class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(GOAL):
            # The characters available to build the string, including a space
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        """Heuristic function to estimate the distance to the goal."""
        # Calculate how many characters are wrong
        wrong = sum(1 for i, char in enumerate(state) if char != GOAL[i])
        # Calculate how many characters are missing
        missing = len(GOAL) - len(state)
        return wrong + missing

# Set up the problem and run the A* search
problem = HelloProblem(initial_state='')
result = astar(problem)

# Print the final state and the path taken
print(result.state)
print(result.path())
