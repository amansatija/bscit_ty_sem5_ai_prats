from collections import defaultdict 

# Define the capacities of the two jugs and the target amount
jug1, jug2, aim = 4, 3, 2 

# Use defaultdict to track visited states to avoid cycles
# Each state is represented as a tuple (amt1, amt2) - the current amounts in each jug
# The default value for any unvisited state is False
visited = defaultdict(lambda: False) 

def waterJugSolver(amt1, amt2): 
    """
    Recursive function to solve the Water Jug problem using depth-first search.
    
    Args:
        amt1: Current amount of water in jug 1
        amt2: Current amount of water in jug 2
        
    Returns:
        True if a solution is found, False otherwise
    """
    # Goal check: Have we reached the target amount in either jug?
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0): 
        print(amt1, amt2)  # Print the final state
        return True         # Solution found!
    
    # Check if this state has been visited before
    if visited[(amt1, amt2)] == False: 
        # Print current state for tracking the solution path
        print(amt1, amt2)  
        
        # Mark current state as visited to avoid cycles
        visited[(amt1, amt2)] = True 
        
        # Try all possible actions from the current state
        # The 'or' chain means we try each action until one leads to a solution
        return (
            # Action 1: Empty jug 1 (set amt1 to 0)
            waterJugSolver(0, amt2) or 
            
            # Action 2: Empty jug 2 (set amt2 to 0)
            waterJugSolver(amt1, 0) or 
            
            # Action 3: Fill jug 1 completely (set amt1 to jug1 capacity)
            waterJugSolver(jug1, amt2) or 
            
            # Action 4: Fill jug 2 completely (set amt2 to jug2 capacity)
            waterJugSolver(amt1, jug2) or 
            
            # Action 5: Pour water from jug 2 to jug 1 (as much as possible)
            # Calculate how much water can be poured: min(water in jug2, space left in jug1)
            # Then update both jugs accordingly
            waterJugSolver(
                amt1 + min(amt2, (jug1 - amt1)),  # New amount in jug1
                amt2 - min(amt2, (jug1 - amt1))   # New amount in jug2
            ) or 
            
            # Action 6: Pour water from jug 1 to jug 2 (as much as possible)
            # Calculate how much water can be poured: min(water in jug1, space left in jug2)
            # Then update both jugs accordingly
            waterJugSolver(
                amt1 - min(amt1, (jug2 - amt2)),  # New amount in jug1
                amt2 + min(amt1, (jug2 - amt2))   # New amount in jug2
            )
        ) 
    else: 
        # We've already visited this state, so backtrack
        return False
    
print("Ahmed Shaikh 323")
print("Steps: ") 
# Start the search with both jugs empty (0, 0)
waterJugSolver(0, 0)


# Let’s unpack:
# Empty jug1: (0, amt2)
# Empty jug2: (amt1, 0)
# Fill jug1: (jug1, amt2)
# Fill jug2: (amt1, jug2)
# Pour jug2 → jug1: # transfer as much as possible into jug1, until jug1 full or jug2 empty
# Pour jug1 → jug2: # transfer as much as possible into jug2, until jug2 full or jug1 empty


# # further details 
# 1. waterJugSolver(0, amt2) → Empty jug1
# We set jug1 to 0 (empty), leave jug2 unchanged.
# Example: (3, 2) → (0, 2).

# 2. waterJugSolver(amt1, 0) → Empty jug2
# We set jug2 to 0, leave jug1 unchanged.
# Example: (3, 2) → (3, 0).

# 3. waterJugSolver(jug1, amt2) → Fill jug1
# We fill jug1 completely to capacity (jug1 = 4 in this problem).
# Example: (1, 2) → (4, 2).

# 4. waterJugSolver(amt1, jug2) → Fill jug2
# We fill jug2 completely to capacity (jug2 = 3).
# Example: (2, 0) → (2, 3).

# 5. waterJugSolver(amt1 + min(amt2, (jug1 - amt1)), amt2 - min(amt2, (jug1 - amt1))) → Pour jug2 → jug1
# This is the pouring logic:
# jug1 - amt1 = remaining space in jug1.
# min(amt2, (jug1 - amt1)) = how much water we can actually pour (can’t pour more than jug2 has, and can’t exceed jug1’s capacity).
# New jug1 = amt1 + poured
# New jug2 = amt2 - poured
# Example: (2, 3) with jug1 capacity 4 →
# Jug1 space = 4 - 2 = 2
# Jug2 has 3, so pour = min(3, 2) = 2
# New state = (2+2, 3-2) = (4, 1) ✅

# 6. waterJugSolver(amt1 - min(amt1, (jug2 - amt2)), amt2 + min(amt1, (jug2 - amt2))) → Pour jug1 → jug2
# Symmetric to step 5 but pour in the opposite direction:
# jug2 - amt2 = remaining space in jug2.
# min(amt1, (jug2 - amt2)) = how much can be poured.
# New jug1 = amt1 - poured
# New jug2 = amt2 + poured
# Example: (3, 1) with jug2 capacity 3 →
# Jug2 space = 3 - 1 = 2
# Jug1 has 3, so pour = min(3, 2) = 2
# New state = (3-2, 1+2) = (1, 3) ✅


# 🔄 Why the or chain?
# Each recursive call returns True if it finds the goal, False otherwise.
# The chain:
# call1 or call2 or call3 ...

# means: try action 1; if it doesn’t solve the problem, try action 2; keep going until one succeeds.
# ✅ So in summary:
# (1–4): Empty/fill operations
# (5–6): Pour operations
# Together, these cover all possible valid actions in the water jug puzzle.