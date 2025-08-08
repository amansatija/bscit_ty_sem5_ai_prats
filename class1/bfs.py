from collections import deque

def bfs_graph(start_node, graph):
    print("ip:start_node:"+start_node)
    print(f"ip:graph:{graph}")
    """
    Perform BFS on a graph.

    Parameters:
    - start_node: The starting node for BFS.
    - graph: The graph represented as an adjacency list (dictionary).

    Returns:
    - A list of nodes in the order they were visited.
    """
    visited = set()      # Set to keep track of visited nodes
    queue = deque([start_node])  # Initialize the queue with the start node
    order = []           # List to keep track of the order of visit

    print(f"bw:visited:{visited}")
    print(f"bw:queue:{queue}")
    print(f"bw:order:{order}")

    while queue:
        node = queue.popleft()  # Dequeue a node from the front of the queue
        print(f"iw:node being proccesed:{node}")
        print(f"iw:queue after processed:{queue}")
        if node not in visited:
            visited.add(node)   # Mark the node as visited
            order.append(node)  # Record the node visit
            print(f"iw:visited after append:{visited}")
            print(f"iw:queue after append :{queue}")
            # Add all unvisited neighbors to the queue
            for neighbor in graph.get(node, []):
                print(f"iwif:neighbour :{neighbor}")
                print(f"iwif:graph  :{graph}")
                if neighbor not in visited:
                    queue.append(neighbor)
                    print(f"iw:queue after processed:{queue}")
    print(f"before returning :order:{order}")
    return order
print("Ahmed Shaikh 323");

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
bfs_order = bfs_graph(start_node, graph)
print("BFS Order:", bfs_order)


# (base) amn@MacBook-Pro-2 class1 % python bfs.py
# Ahmed Shaikh 323
# ip:start_node:A
# ip:graph:{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# bw:visited:set()
# bw:queue:deque(['A'])
# bw:order:[]
# iw:node being proccesed:A
# iw:queue after processed:deque([])
# iw:visited after append:{'A'}
# iw:queue after append :deque([])
# iwif:neighbour :B
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iw:queue after processed:deque(['B'])
# iwif:neighbour :C
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iw:queue after processed:deque(['B', 'C'])
# iw:node being proccesed:B
# iw:queue after processed:deque(['C'])
# iw:visited after append:{'A', 'B'}
# iw:queue after append :deque(['C'])
# iwif:neighbour :A
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iwif:neighbour :D
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iw:queue after processed:deque(['C', 'D'])
# iwif:neighbour :E
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iw:queue after processed:deque(['C', 'D', 'E'])
# iw:node being proccesed:C
# iw:queue after processed:deque(['D', 'E'])
# iw:visited after append:{'A', 'B', 'C'}
# iw:queue after append :deque(['D', 'E'])
# iwif:neighbour :A
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iwif:neighbour :F
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iw:queue after processed:deque(['D', 'E', 'F'])
# iw:node being proccesed:D
# iw:queue after processed:deque(['E', 'F'])
# iw:visited after append:{'A', 'B', 'C', 'D'}
# iw:queue after append :deque(['E', 'F'])
# iwif:neighbour :B
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iw:node being proccesed:E
# iw:queue after processed:deque(['F'])
# iw:visited after append:{'D', 'E', 'B', 'C', 'A'}
# iw:queue after append :deque(['F'])
# iwif:neighbour :B
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iwif:neighbour :F
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iw:queue after processed:deque(['F', 'F'])
# iw:node being proccesed:F
# iw:queue after processed:deque(['F'])
# iw:visited after append:{'D', 'E', 'B', 'C', 'F', 'A'}
# iw:queue after append :deque(['F'])
# iwif:neighbour :C
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iwif:neighbour :E
# iwif:graph  :{'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# iw:node being proccesed:F
# iw:queue after processed:deque([])
# before returning :order:['A', 'B', 'C', 'D', 'E', 'F']
# BFS Order: ['A', 'B', 'C', 'D', 'E', 'F']