import heapq

def dijkstra(graph, start):
    """
    Finds the shortest paths from the start node to all other nodes in a weighted graph.
    
    Args:
        graph: A dictionary where keys are nodes and values are dictionaries of neighbors and weights.
               Example: {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, ...}
        start: The starting node.

    Returns:
        A dictionary containing the shortest distance from the start node to each node.
    """
    # distances[node] = shortest distance from start to node known so far
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Priority queue to store tuples of (distance, node)
    # The heap property ensures we always explore the node with the smallest distance first
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we found a longer path to this node than we already recorded, skip it
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If this path is shorter than any previously recorded path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    # Example Graph
    example_graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start_node = 'A'
    results = dijkstra(example_graph, start_node)
    
    print(f"Shortest distances from node {start_node}:")
    for node, distance in results.items():
        print(f"Node {node}: {distance}")
