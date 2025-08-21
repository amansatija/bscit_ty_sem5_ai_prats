import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

class Node:
    def __init__(self, name, children=None, value=None):
        self.name = name
        self.children = children if children is not None else []
        self.value = value

def draw_tree():
    # Create the game tree (same as your structure)
    D = Node('D', value=3)
    E = Node('E', value=5)
    F = Node('F', value=6)
    G = Node('G', value=9)
    H = Node('H', value=1)
    I = Node('I', value=2)

    B = Node('B', children=[D, E, F])
    C = Node('C', children=[G, H, I])

    A = Node('A', children=[B, C])

    # Set up the plot
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Define positions for each node
    positions = {
        'A': (5, 7),
        'B': (2.5, 5),
        'C': (7.5, 5),
        'D': (1, 3),
        'E': (2.5, 3),
        'F': (4, 3),
        'G': (6, 3),
        'H': (7.5, 3),
        'I': (9, 3)
    }

    # Define node colors
    colors = {
        'A': '#e1f5fe',  # Light blue for root
        'B': '#f3e5f5',  # Light purple for internal nodes
        'C': '#f3e5f5',  # Light purple for internal nodes
        'D': '#e8f5e8',  # Light green for leaf nodes
        'E': '#e8f5e8',
        'F': '#e8f5e8',
        'G': '#e8f5e8',
        'H': '#e8f5e8',
        'I': '#e8f5e8'
    }

    # Draw connections first (so they appear behind nodes)
    connections = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'), ('B', 'F'),
        ('C', 'G'), ('C', 'H'), ('C', 'I')
    ]

    for parent, child in connections:
        x1, y1 = positions[parent]
        x2, y2 = positions[child]
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=2, alpha=0.7)

    # Draw nodes
    nodes_data = {
        'A': {'value': None, 'type': 'root'},
        'B': {'value': None, 'type': 'internal'},
        'C': {'value': None, 'type': 'internal'},
        'D': {'value': 3, 'type': 'leaf'},
        'E': {'value': 5, 'type': 'leaf'},
        'F': {'value': 6, 'type': 'leaf'},
        'G': {'value': 9, 'type': 'leaf'},
        'H': {'value': 1, 'type': 'leaf'},
        'I': {'value': 2, 'type': 'leaf'}
    }

    for node_name, data in nodes_data.items():
        x, y = positions[node_name]
        
        # Create fancy box for node
        if data['type'] == 'leaf':
            # For leaf nodes, show both name and value
            text = f"{node_name}\n({data['value']})"
            box_height = 0.6
        else:
            # For internal nodes, show only name
            text = node_name
            box_height = 0.4
        
        # Draw the node box
        fancy_box = FancyBboxPatch(
            (x-0.3, y-box_height/2), 0.6, box_height,
            boxstyle="round,pad=0.1",
            facecolor=colors[node_name],
            edgecolor='black',
            linewidth=2
        )
        ax.add_patch(fancy_box)
        
        # Add text
        ax.text(x, y, text, ha='center', va='center', 
                fontsize=12, fontweight='bold')

    # Add title and labels
    ax.text(5, 7.7, 'Game Tree Structure', ha='center', va='center', 
            fontsize=16, fontweight='bold')
    
    # Add legend
    legend_elements = [
        patches.Patch(color='#e1f5fe', label='Root Node'),
        patches.Patch(color='#f3e5f5', label='Internal Nodes'),
        patches.Patch(color='#e8f5e8', label='Leaf Nodes (with values)')
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.98, 0.98))

    # Add level labels
    ax.text(0.2, 7, 'Level 0', ha='center', va='center', fontsize=10, 
            style='italic', alpha=0.7)
    ax.text(0.2, 5, 'Level 1', ha='center', va='center', fontsize=10, 
            style='italic', alpha=0.7)
    ax.text(0.2, 3, 'Level 2', ha='center', va='center', fontsize=10, 
            style='italic', alpha=0.7)

    plt.tight_layout()
    plt.savefig('/Users/amn/amn_local/dev/projects/credibleinc/inhouse/teach/bscit_sem5_ai_practicals_ameen/workspace/practice/class4/tree_diagram.png', 
                dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    draw_tree()
