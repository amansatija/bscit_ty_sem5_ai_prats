# Water Jug Problem Explanation

## Problem Statement
We have two jugs with capacities of 4 liters and 3 liters (no markings on the jugs).
We need to measure exactly 2 liters of water using these jugs.

## Recursive Solution Approach

The solution uses a depth-first search (DFS) approach with backtracking to explore all possible states until we find a solution.

### State Representation
- Each state is represented as a tuple `(amt1, amt2)` where:
  - `amt1` = amount of water in the 4-liter jug
  - `amt2` = amount of water in the 3-liter jug

### Possible Actions
From any state, we can perform six possible actions:
1. **Empty jug 1**: `(amt1, amt2)` → `(0, amt2)`
2. **Empty jug 2**: `(amt1, amt2)` → `(amt1, 0)`
3. **Fill jug 1**: `(amt1, amt2)` → `(4, amt2)`
4. **Fill jug 2**: `(amt1, amt2)` → `(amt1, 3)`
5. **Pour jug 2 into jug 1**: Transfer as much water as possible from jug 2 to jug 1
6. **Pour jug 1 into jug 2**: Transfer as much water as possible from jug 1 to jug 2

### Algorithm Steps
1. Start with both jugs empty: `(0, 0)`
2. Try each of the six possible actions
3. For each new state:
   - Check if it's the goal state (2 liters in either jug)
   - Check if we've visited this state before (to avoid cycles)
   - If not visited, mark it as visited and recursively try all actions from this state
4. Use backtracking when we reach a dead end (all states from current state have been visited)

### The "or" Chain Explained
The recursive function uses an "or" chain of function calls:
```python
return (action1() or action2() or action3() or action4() or action5() or action6())
```

This means:
- Try action1; if it leads to a solution, return True
- Otherwise, try action2; if it leads to a solution, return True
- And so on...
- If none of the actions lead to a solution, return False

## Visual Representation of State Transitions

```
Initial State: (0, 0) [Both jugs empty]
                  |
                  v
        +----+----+----+----+----+----+
        |    |    |    |    |    |    |
        v    v    v    v    v    v    v
Empty1 Empty2 Fill1 Fill2 Pour2→1 Pour1→2
(0,0)  (0,0)  (4,0) (0,3) (0,0)   (0,0)
        X     X
```

Let's follow one possible solution path:

```
(0,0) → Fill jug 2 → (0,3)
(0,3) → Pour jug 2 into jug 1 → (3,0)
(3,0) → Fill jug 2 → (3,3)
(3,3) → Pour jug 2 into jug 1 → (4,2)
(4,2) → Empty jug 1 → (0,2)
```

At state `(0,2)`, we have 2 liters in jug 2, which is our goal!

## Avoiding Cycles
The algorithm uses a `visited` dictionary to keep track of states we've already explored. This prevents infinite loops and ensures the algorithm terminates.

## Pouring Logic Explained

### Pour from jug 2 to jug 1:
```python
amt1 + min(amt2, (jug1 - amt1)), amt2 - min(amt2, (jug1 - amt1))
```

- `jug1 - amt1`: Space available in jug 1
- `min(amt2, (jug1 - amt1))`: Amount that can be poured (minimum of water in jug 2 and space in jug 1)
- New amount in jug 1: Current amount + poured amount
- New amount in jug 2: Current amount - poured amount

### Pour from jug 1 to jug 2:
```python
amt1 - min(amt1, (jug2 - amt2)), amt2 + min(amt1, (jug2 - amt2))
```

- `jug2 - amt2`: Space available in jug 2
- `min(amt1, (jug2 - amt2))`: Amount that can be poured (minimum of water in jug 1 and space in jug 2)
- New amount in jug 1: Current amount - poured amount
- New amount in jug 2: Current amount + poured amount
