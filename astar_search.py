import heapq

def astar(grid, start, goal):
    """
    A* search algorithm to find the shortest path in a grid.
    grid: 2D list where 0 is walkable and 1 is an obstacle.
    start: (row, col)
    goal: (row, col)
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Priority queue: (f_score, (row, col))
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in get_neighbors(current, rows, cols):
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue
                
            tentative_g_score = g_score[current] + 1
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in [item[1] for item in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    
    return None

def heuristic(p1, p2):
    # Manhattan distance
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_neighbors(pos, rows, cols):
    r, c = pos
    neighbors = []
    if r > 0: neighbors.append((r-1, c))
    if r < rows - 1: neighbors.append((r+1, c))
    if c > 0: neighbors.append((r, c-1))
    if c < cols - 1: neighbors.append((r, c+1))
    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)
    path = astar(grid, start, goal)
    print(f"Path found: {path}")
