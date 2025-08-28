import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def create_alpha_beta_visualization():
    """
    Creates a visual representation of the Alpha-Beta pruning algorithm
    using the example tree from alphabetasearch.py
    """
    # Create a directed graph
    G = nx.DiGraph()
    
    # Define node positions manually for a clean tree layout
    pos = {
        'A': (0, 0),
        'B': (-3, -2), 'C': (3, -2),
        'D': (-4.5, -4), 'E': (-1.5, -4), 'F': (1.5, -4), 'G': (4.5, -4),
        'H': (-5, -6), 'I': (-4, -6), 'J': (-2, -6), 'K': (-1, -6), 'L': (1, -6), 'M': (2, -6), 'N': (4, -6), 'O': (5, -6)
    }
    
    # Add nodes with labels
    G.add_node('A', label='MAX')
    G.add_node('B', label='MIN')
    G.add_node('C', label='MIN')
    G.add_node('D', label='MAX')
    G.add_node('E', label='MAX')
    G.add_node('F', label='MAX')
    G.add_node('G', label='MAX')
    G.add_node('H', label='5')
    G.add_node('I', label='1')
    G.add_node('J', label='2')
    G.add_node('K', label='8')
    G.add_node('L', label='-8')
    G.add_node('M', label='-9')
    G.add_node('N', label='9')
    G.add_node('O', label='4')
    
    # Add edges
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'), ('C', 'G'),
        ('D', 'H'), ('D', 'I'), ('D', 'J'),
        ('E', 'K'), ('E', 'L'), ('E', 'M'),
        ('F', 'N'), ('F', 'O')
    ]
    G.add_edges_from(edges)
    
    # Create the figure
    plt.figure(figsize=(12, 8))
    
    # Draw the graph
    nx.draw(G, pos, with_labels=False, node_size=1200, node_color='lightblue', 
            font_size=10, font_weight='bold', arrowsize=15)
    
    # Draw node labels
    node_labels = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12)
    
    # Add alpha-beta annotations
    annotations = [
        ((-5.3, -6), "α=5"),
        ((-4.3, -6), "α=5"),
        ((-4.8, -4), "α=5"),
        ((-2.3, -6), "α=2"),
        ((-1.3, -6), "α=8"),
        ((-1.8, -4), "α=8"),
        ((-3, -2), "β=5"),
        ((1.3, -6), "β=-8"),
        ((2.3, -6), "β=-9"),
        ((1.8, -4), "β=-8"),
        ((4.3, -6), "α=9"),
        ((4.8, -4), "α=9"),
        ((3, -2), "β=-8"),
        ((0, 0), "α=5")
    ]
    
    # Add pruning indicators
    pruned_edges = [('G', 'P'), ('G', 'Q')]  # These nodes don't exist but show where pruning happens
    
    # Add text annotations for alpha-beta values
    for pos, text in annotations:
        plt.text(pos[0], pos[1], text, fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
    
    # Add text for pruned branches
    plt.text(5, -6, "PRUNED", fontsize=12, color='red', 
             bbox=dict(facecolor='white', alpha=0.7))
    
    # Add title and explanation
    plt.title("Alpha-Beta Pruning Algorithm Visualization", fontsize=16)
    
    # Add explanation text
    explanation = """
    Alpha-Beta Pruning Algorithm:
    - MAX nodes (even depth): Choose maximum of children, update α
    - MIN nodes (odd depth): Choose minimum of children, update β
    - Prune when α ≥ β (no need to explore further branches)
    - Initial values: α = -∞, β = +∞
    """
    plt.figtext(0.5, -0.05, explanation, ha="center", fontsize=12, 
                bbox=dict(facecolor='white', alpha=0.8))
    
    # Save the figure
    plt.savefig('/Users/amn/amn_local/dev/projects/credibleinc/inhouse/teach/bscit_sem5_ai_practicals_ameen/workspace/practice/class4/alpha_beta_tree.png', 
                bbox_inches='tight', dpi=300)
    plt.close()
    
    print("Alpha-Beta pruning visualization created and saved as 'alpha_beta_tree.png'")

if __name__ == "__main__":
    create_alpha_beta_visualization()
