from collections import deque

def bfs(graph, start_node):
    """
    Perform Breadth-First Search on a graph starting from start_node.
    
    Args:
        graph: Dictionary where keys are nodes and values are lists of neighbors.
        start_node: The node to start the search from.
        
    Returns:
        A list of nodes in the order they were visited.
    """
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    example_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("BFS Traversal starting from node 'A':")
    print(bfs(example_graph, 'A'))
