import heapq

class Node:
    def __init__(self, name, g_cost=0, h_cost=0):
        self.name = name
        self.g_cost = g_cost  # Cost from start to this node
        self.h_cost = h_cost  # Heuristic cost from this node to the goal
        self.f_cost = g_cost + h_cost  # Total cost (g_cost + h_cost)
        self.parent = None

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def a_star_search(start, goal, graph):
    open_list = []
    closed_list = set()
    
    start_node = Node(start, 0, graph[start]['heuristic'])
    goal_node = Node(goal)
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.name == goal_node.name:
            return reconstruct_path(current_node)
        
        closed_list.add(current_node.name)
        
        for neighbor, (cost, heuristic) in graph[current_node.name]['neighbors'].items():
            if neighbor in closed_list:
                continue
            
            g_cost = current_node.g_cost + cost
            h_cost = heuristic
            neighbor_node = Node(neighbor, g_cost, h_cost)
            neighbor_node.parent = current_node
            
            if any(node.name == neighbor and node.f_cost <= neighbor_node.f_cost for node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)
    
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]

# Example usage:
graph = {
    'A': {'neighbors': {'B': (1, 2), 'C': (4, 1)}, 'heuristic': 3},
    'B': {'neighbors': {'D': (2, 1), 'E': (5, 0)}, 'heuristic': 2},
    'C': {'neighbors': {'F': (3, 0)}, 'heuristic': 1},
    'D': {'neighbors': {}, 'heuristic': 0},
    'E': {'neighbors': {}, 'heuristic': 0},
    'F': {'neighbors': {'D': (1, 0)}, 'heuristic': 0},
}

start = 'A'
goal = 'D'
path = a_star_search(start, goal, graph)
print(f"Path found: {path}")
