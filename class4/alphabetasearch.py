class Node:
    def __init__(self, name, children=None, value=None):
        self.name = name
        self.children = children if children is not None else []
        self.value = value

def evaluate(node):
    return node.value

def is_terminal(node):
    return node.value is not None

def get_children(node):
    return node.children

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    id = ""+node.name+str(depth)+str(alpha)+str(beta)+str(maximizing_player)
    print(f"called alpha_beta_pruning({node.name}, {depth}, {alpha}, {beta}, {maximizing_player})")
    if depth == 0 or is_terminal(node):
        print(f"fromm first check ::{depth}, {node.name}")
        return evaluate(node)
    
    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(node):
            eval = alpha_beta_pruning(child, depth-1, alpha, beta, False)
            print(f"returned eval for  {id} == {eval}")
            print(f"current alpha before max comparison for  {id} == {alpha}")
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            print(f"setting alpha before min comparison for  {id}")
            print(f"current alpha after max comparison for  {id} == {alpha}")
            print(f"current beta after max comparison for  {id} == {beta}")
            if beta <= alpha:
                print(f"Pruning .. after max comparison for  {id} == {alpha}")
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(node):
            eval = alpha_beta_pruning(child, depth-1, alpha, beta, True)
            print(f"returned eval for  {id} == {eval}")
            print(f"current beta  before min comparison for  {id} == {beta}")
            min_eval = min(min_eval, eval)
            
            beta = min(beta, eval)
            print(f"setting beta before min comparison for  {id}")
            print(f"current beta after min comparison for  {id} == {beta}")
            print(f"current alpha after min comparison for  {id} == {alpha}")
            if beta <= alpha:
                print(f"Pruning .. after min comparison for  {id} == {alpha}")
                break  # Alpha cut-off
        return min_eval

# Create the game tree
D = Node('D', value=3)
E = Node('E', value=5)
F = Node('F', value=6)
G = Node('G', value=9)
H = Node('H', value=1)
I = Node('I', value=2)

B = Node('B', children=[D, E, F])
C = Node('C', children=[G, H, I])

A = Node('A', children=[B, C])

# Run the alpha-beta pruning algorithm
maximizing_player = True
initial_alpha = float('-inf')
initial_beta = float('inf')
depth = 3  # Maximum depth of the tree

optimal_value = alpha_beta_pruning(A, depth, initial_alpha, initial_beta, maximizing_player)
print(f"The optimal value is: {optimal_value}")




# Based on the execution trace, 3 is the optimal value because of how the minimax algorithm with alpha-beta pruning works. Let me explain step by step:

# Tree Structure & Player Roles
# A (root): Maximizing player (wants highest value)
# B, C (level 1): Minimizing players (want lowest value)
# D,E,F,G,H,I (leaves): Terminal nodes with values [3,5,6,9,1,2]
# Execution Analysis
# Step 1: Evaluating Subtree B
# B is a minimizing node with children D(3), E(5), F(6)
# B chooses the minimum: min(3,5,6) = 3
# A's alpha becomes 3
# Step 2: Evaluating Subtree C
# C is a minimizing node with children G(9), H(1), I(2)
# C evaluates G(9) first → beta becomes 9
# C evaluates H(1) next → beta becomes min(9,1) = 1
# Pruning occurs: Since beta(1) ≤ alpha(3), node I is pruned
# C returns 1
# Step 3: A's Final Decision
# A (maximizing) compares: max(3, 1) = 3
# A chooses the path through B, which gives value 3
# Why 3 is Optimal
# The algorithm proves that 3 is the best achievable value for the maximizing player because:

# From subtree B: The minimizing opponent will choose 3 (best they can do is limit max player to 3)
# From subtree C: The minimizing opponent will choose 1 (even worse for max player)
# Rational choice: The maximizing player picks B's path (value 3) over C's path (value 1)
# The alpha-beta pruning correctly eliminated exploring node I because it was already proven that C's subtree couldn't offer anything better than what B already guaranteed.