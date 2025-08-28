# Alpha-Beta Pruning Algorithm Explanation

## Overview
Alpha-Beta pruning is an optimization technique for the minimax algorithm used in game theory and decision-making. It significantly reduces the number of nodes evaluated in the search tree by eliminating branches that cannot influence the final decision.

## Key Concepts

- **Alpha (α)**: Best value that the maximizing player (MAX) can guarantee
- **Beta (β)**: Best value that the minimizing player (MIN) can guarantee
- **Pruning**: Skipping evaluation of branches that cannot affect the final decision

## How the Algorithm Works with Our Example Tree

Our tree is represented as: `[[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]`

This corresponds to the following game tree structure:

```
                A (MAX)
              /       \
             /         \
            B (MIN)     C (MIN)
           /  \         /  \
          /    \       /    \
         D      E     F      G
        /|\    /|\   /|\    /|\
       5 1 2  8 -8 -9 9 4 5 -3 4 3
```

### Step-by-Step Execution

1. **Initialize**: α = -∞, β = +∞ at the root node A (MAX)

2. **Process left subtree (B)**:
   - At node B (MIN), α = -∞, β = +∞
   - Process node D (MAX):
     - Evaluate leaf 5: α = max(-∞, 5) = 5
     - Evaluate leaf 1: α = max(5, 1) = 5
     - Evaluate leaf 2: α = max(5, 2) = 5
     - Return α = 5 to node B
   - At node B, β = min(+∞, 5) = 5
   - Process node E (MAX):
     - Evaluate leaf 8: α = max(-∞, 8) = 8
     - Evaluate leaf -8: α = max(8, -8) = 8
     - Evaluate leaf -9: α = max(8, -9) = 8
     - Return α = 8 to node B
   - At node B, β = min(5, 8) = 5
   - Return β = 5 to node A

3. **At node A (MAX)**, α = max(-∞, 5) = 5

4. **Process right subtree (C)**:
   - At node C (MIN), α = 5, β = +∞
   - Process node F (MAX):
     - Evaluate leaf 9: α = max(-∞, 9) = 9
     - Evaluate leaf 4: α = max(9, 4) = 9
     - Return α = 9 to node C
   - At node C, β = min(+∞, 9) = 9
   - Process node G (MAX):
     - Evaluate leaf -3: α = max(-∞, -3) = -3
     - **Pruning occurs**: Since α = 5 at node A and β = -3 at node G, we have α > β
     - No need to evaluate remaining leaves (4, 3) in node G
   - At node C, β = min(9, -3) = -3
   - Return β = -3 to node A

5. **Final result at node A (MAX)**: α = max(5, -3) = 5

### Pruning Explanation

In our example, pruning occurs at node G. After evaluating the first leaf (-3), we know that:
- The MAX player at node A already has a guaranteed value of 5
- The MIN player at node C will choose at most -3 from node G
- Since 5 > -3, the MAX player will never choose the path through node G
- Therefore, we can skip evaluating the remaining leaves (4, 3) at node G

This is the essence of Alpha-Beta pruning: avoiding unnecessary evaluations when we can prove they won't affect the final decision.

## The Line of Code in Question

```python
branch[i] = alpha if depth % 2 == 0 else beta
```

This line updates the value of the current branch based on whether we're at a MAX level (even depth) or MIN level (odd depth):
- At MAX levels (depth % 2 == 0), we store the alpha value (best for MAX)
- At MIN levels (depth % 2 == 1), we store the beta value (best for MIN)

This ensures that as we backtrack through the tree, each node gets updated with the appropriate value based on whether it's a MAX or MIN node.
