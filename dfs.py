from collections import defaultdict


def dfs_iterative(graph, start_node):
    """
    Perform iterative Depth-First Search on a graph.

    Args:
        graph: Dictionary where keys are nodes and values are lists of neighbors.
        start_node: The node to start the search from.

    Returns:
        A list of nodes in the order they were visited.
    """
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            # Add neighbors in reverse order so left-most neighbor is visited first
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order


def dfs_recursive(graph, start_node, visited=None):
    """
    Perform recursive Depth-First Search on a graph.

    Args:
        graph: Dictionary where keys are nodes and values are lists of neighbors.
        start_node: The node to start the search from.
        visited: Set of already-visited nodes (used internally by recursion).

    Returns:
        A list of nodes in the order they were visited.
    """
    if visited is None:
        visited = set()

    visited.add(start_node)
    traversal_order = [start_node]

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            traversal_order.extend(dfs_recursive(graph, neighbor, visited))

    return traversal_order


def dfs_find_path(graph, start, end, visited=None):
    """
    Find a path between start and end nodes using DFS.

    Returns:
        A list representing the path, or None if no path exists.
    """
    if visited is None:
        visited = set()

    visited.add(start)

    if start == end:
        return [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs_find_path(graph, neighbor, end, visited)
            if path is not None:
                return [start] + path

    return None


if __name__ == "__main__":
    example_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("=== Depth-First Search ===\n")
    print("Iterative DFS from 'A':", dfs_iterative(example_graph, 'A'))
    print("Recursive DFS from 'A':", dfs_recursive(example_graph, 'A'))

    print("\n=== Path Finding (DFS) ===")
    path = dfs_find_path(example_graph, 'A', 'F')
    print(f"Path from A to F: {' -> '.join(path) if path else 'No path found'}")

    path2 = dfs_find_path(example_graph, 'D', 'C')
    print(f"Path from D to C: {' -> '.join(path2) if path2 else 'No path found'}")
