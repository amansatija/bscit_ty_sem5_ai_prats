import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# Sample game tree represented as a nested list structure
# Each leaf node represents a utility value (score)
tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]

# Starting depth of the tree (0 = root)
root = 0

# Counter for pruned branches
pruned = 0

# Enable/disable debug prints
DEBUG = True

# Function to print indented debug messages based on depth
def debug_print(depth, message):
    if DEBUG:
        indent = "  " * depth
        logging.info(f"{indent}{message}")

def children(branch, depth, alpha, beta):
    """
    Implements the Alpha-Beta pruning algorithm on a game tree.
    
    Args:
        branch: Current branch/node in the game tree
        depth: Current depth in the tree (0 = root)
        alpha: Best value for MAX player found so far
        beta: Best value for MIN player found so far
    
    Returns:
        tuple: Updated (alpha, beta) values after processing this branch
    """
    global tree
    global root
    global pruned
    i = 0  # Index to track position in the branch list
    
    # Print node information
    node_type = "MAX" if depth % 2 == 0 else "MIN"
    debug_print(depth, f"Entering {node_type} node at depth {depth}")
    debug_print(depth, f"Initial α={alpha}, β={beta}")
    debug_print(depth, f"Node value: {branch}")
    
    # Iterate through each child of the current branch
    for child_index, child in enumerate(branch):
        debug_print(depth, f"Examining child {child_index}: {child}")
        
        # If child is a list, it's an internal node - recurse deeper
        if isinstance(child, list):
            debug_print(depth, f"Child {child_index} is an internal node, recursing deeper...")
            
            # Recursive call to process child branch
            old_alpha, old_beta = alpha, beta
            nalpha, nbeta = children(child, depth + 1, alpha, beta)
            debug_print(depth, f"Returned from recursion with α={nalpha}, β={nbeta}")
            
            # Update alpha/beta based on depth (MIN or MAX level)
            if depth % 2 == 1:  # MIN level (odd depth)
                old_beta = beta
                beta = min(beta, nalpha)  # MIN player wants to minimize
                if beta != old_beta:
                    debug_print(depth, f"MIN node: Updated β from {old_beta} to {beta}")
            else:  # MAX level (even depth)
                old_alpha = alpha
                alpha = max(alpha, nbeta)  # MAX player wants to maximize
                if alpha != old_alpha:
                    debug_print(depth, f"MAX node: Updated α from {old_alpha} to {alpha}")
            
            # Update the branch with the appropriate value (alpha for MAX, beta for MIN)
            old_value = branch[i] if i < len(branch) else "None"
            branch[i] = alpha if depth % 2 == 0 else beta
            debug_print(depth, f"Updated branch[{i}] from {old_value} to {branch[i]}")
            i += 1
        else:
            # If child is a leaf node (actual value)
            debug_print(depth, f"Child {child_index} is a leaf node with value {child}")
            
            if depth % 2 == 0:  # MAX level
                old_alpha = alpha
                if alpha < child:
                    alpha = child
                    debug_print(depth, f"MAX node: Leaf value {child} > α={old_alpha}, updating α to {alpha}")
                else:
                    debug_print(depth, f"MAX node: Leaf value {child} <= α={alpha}, no update")
            
            if depth % 2 == 1:  # MIN level
                old_beta = beta
                if beta > child:
                    beta = child
                    debug_print(depth, f"MIN node: Leaf value {child} < β={old_beta}, updating β to {beta}")
                else:
                    debug_print(depth, f"MIN node: Leaf value {child} >= β={beta}, no update")
        
        # Alpha-Beta pruning condition: if alpha >= beta, prune the remaining branches
        if alpha >= beta:
            pruned += 1  # Count pruned branches
            debug_print(depth, f"PRUNING! α={alpha} >= β={beta}")
            debug_print(depth, f"Skipping remaining children: {branch[i+1:]}")
            break  # Skip remaining children
    
    # If we're back at the root, update the final result
    if depth == root:
        old_tree = tree
        tree = alpha if root == 0 else beta
        debug_print(depth, f"Back at root. Final result: {tree}")
    
    debug_print(depth, f"Exiting node at depth {depth} with final α={alpha}, β={beta}")
    debug_print(depth, "")
    
    # Return updated alpha and beta values
    return alpha, beta

print("Ahmed Shaikh 323")

def alphabeta(debug_mode=True):
    """
    Main function to start the Alpha-Beta pruning algorithm.
    Initializes alpha to negative infinity and beta to positive infinity.
    Prints the final result and number of pruned branches.
    
    Args:
        debug_mode: Whether to print detailed debug information
    """
    global tree
    global pruned
    global root
    global DEBUG
    
    # Set debug mode
    DEBUG = debug_mode
    
    # Print initial tree
    if DEBUG:
        logging.info("\n==== ALPHA-BETA PRUNING ALGORITHM ====\n")
        logging.info(f"Initial tree: {tree}")
        logging.info(f"Starting with α=-∞, β=+∞\n")
    
    # Run the algorithm
    alpha, beta = children(tree, root, -float('inf'), float('inf'))
    
    # Print results
    logging.info("\n==== RESULTS ====\n")
    logging.info(f"Final (alpha, beta): {alpha}, {beta}")
    logging.info(f"Result: {tree}")
    logging.info(f"Branches pruned: {pruned}")
    
    # Print a visual representation of the pruning efficiency
    if DEBUG:
        logging.info("\n==== PRUNING EFFICIENCY ====\n")
        total_nodes = count_nodes(tree)
        logging.info(f"Total nodes in tree: {total_nodes}")
        logging.info(f"Nodes pruned: {pruned}")
        logging.info(f"Efficiency: {pruned/total_nodes:.2%} of branches pruned")
    
    return alpha, beta, tree, pruned


def count_nodes(branch):
    """Helper function to count the total number of nodes in the tree"""
    if not isinstance(branch, list):
        return 1
    
    count = 1  # Count this node
    for child in branch:
        count += count_nodes(child)
    
    return count

if __name__ == "__main__":
    # Run with debug prints
    alphabeta(debug_mode=True)
    
    # Uncomment to run without debug prints
    # alphabeta(debug_mode=False)