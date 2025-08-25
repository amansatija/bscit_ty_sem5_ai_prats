import heapq # Used for the open list, as it provides efficient retrieval of the lowest-cost element.

class Node:
    """
    Represents a node in the grid for the A* algorithm.
    Each node stores its position, cost values, and a reference to its parent.
    """
    def __init__(self, position, parent=None):
        self.position = position  # Tuple (row, col)
        self.parent = parent      # Reference to the parent node

        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic (estimated cost from this node to end)
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        """Compares two nodes based on their position."""
        return self.position == other.position

    def __hash__(self):
        """Makes node objects hashable, so they can be stored in sets (like the closed list)."""
        return hash(self.position)

    def __lt__(self, other):
        """
        Allows nodes to be compared based on their f-cost,
        which is necessary for heapq (priority queue).
        """
        return self.f < other.f

    def __repr__(self):
        """String representation for debugging."""
        return f"Node(pos={self.position}, f={self.f}, g={self.g}, h={self.h})"

def heuristic(node_pos, goal_pos):
    """
    Calculates the Manhattan distance heuristic between two points.
    Manhattan distance is admissible for grid-based movement (up, down, left, right).
    """
    return abs(node_pos[0] - goal_pos[0]) + abs(node_pos[1] - goal_pos[1])

def a_star(grid, start, end):
    """
    Finds the shortest path from start to end using the A* algorithm.

    Args:
        grid (list of lists): A 2D list representing the maze/map.
                              0 represents a traversable path, 1 represents an obstacle.
        start (tuple): The (row, col) coordinates of the starting point.
        end (tuple): The (row, col) coordinates of the ending point.

    Returns:
        list of tuples: The path as a list of (row, col) coordinates,
                        or None if no path is found.
    """

    # Create start and end nodes
    start_node = Node(start)
    end_node = Node(end)

    # Initialize open and closed lists
    # The open list is a priority queue (min-heap) to efficiently get the node with the lowest f-cost.
    open_list = []
    heapq.heappush(open_list, start_node)

    # The closed list stores nodes that have already been evaluated.
    # Using a set for faster lookup of visited nodes.
    closed_list_positions = set() # Store only positions for quick lookup
    # To reconstruct path, we need to store the actual Node objects in the closed list
    # or ensure parent pointers are correctly set in nodes in the open list.
    # We will rely on parent pointers and rebuild from the `current_node` once goal is reached.
    # The `closed_list_positions` set is enough for checking if a node has been fully processed.

    # Grid dimensions
    rows, cols = len(grid), len(grid[0])

    # Possible movements (up, down, left, right)
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)] # (row_change, col_change)

    while open_list:
        # Get the node with the lowest f-cost from the open list
        current_node = heapq.heappop(open_list)
        current_pos = current_node.position
        print(f"current_node = {current_node}")
        print(f"current_pos = {current_pos}")
        # Add current node's position to the closed list
        closed_list_positions.add(current_pos)
        print(f"closed_list_positions = {closed_list_positions}")
        # Check if we reached the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path (from start to end)

        # Explore neighbors
        for move in movements:
            neighbor_pos = (current_pos[0] + move[0], current_pos[1] + move[1])

            # Check if neighbor is within grid boundaries
            if not (0 <= neighbor_pos[0] < rows and 0 <= neighbor_pos[1] < cols):
                continue

            # Check if neighbor is an obstacle (grid[row][col] == 1)
            if grid[neighbor_pos[0]][neighbor_pos[1]] == 1:
                continue

            # Check if neighbor is already in the closed list
            if neighbor_pos in closed_list_positions:
                continue

            # Create a new node for the neighbor
            neighbor = Node(neighbor_pos, current_node)

            # Calculate g, h, and f values for the neighbor
            # Assuming a cost of 1 for moving to an adjacent cell
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, end_node.position)
            neighbor.f = neighbor.g + neighbor.h

            # Check if neighbor is already in the open list with a higher g-cost
            # If so, we found a better path to it, so update it.
            # Python's heapq doesn't directly support efficient update,
            # so we'll push the new, better path. Duplicates will be handled
            # because we only process the one with the lowest f-cost from the heap,
            # and ignore others if their position is already in the closed list.
            found_in_open = False
            for open_node in open_list:
                if open_node == neighbor and open_node.g <= neighbor.g:
                    found_in_open = True
                    break

            if not found_in_open:
                heapq.heappush(open_list, neighbor)

    # If open list is empty and goal was not reached, no path exists
    return None

# --- Example Usage ---
if __name__ == "__main__":
    # Define a sample grid (0 = path, 1 = obstacle)
    grid = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    start_point = (0, 0) # Start at top-left
    end_point = (9, 9)   # End at bottom-right

    print(f"Finding path from {start_point} to {end_point}...")
    path = a_star(grid, start_point, end_point)

    if path:
        print("Path found:")
        for r, c in path:
            grid[r][c] = '*' # Mark path on grid
        for row in grid:
            print(" ".join(map(str, row)))
    else:
        print("No path found!")

    print("\n--- Another Example (Unreachable) ---")
    grid_unreachable = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    start_unreachable = (0, 0)
    end_unreachable = (2, 2)
    path_unreachable = a_star(grid_unreachable, start_unreachable, end_unreachable)
    if path_unreachable:
        print("Path found (unreachable example):", path_unreachable)
    else:
        print("No path found for unreachable example!")

