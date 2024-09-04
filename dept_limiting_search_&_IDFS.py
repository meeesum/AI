class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        if w not in self.adj:
            self.adj[w] = []
        self.adj[v].append(w)

    def get_neighbors(self, v):
        return self.adj.get(v, [])

def depth_limited_search(graph, start, goal, depth_limit):
    def dls(v, goal, limit):
        print(f"Visiting Node {v}, Depth Limit {limit}")

        if v == goal:
            return True
        if limit <= 0:
            return False

        for neighbor in graph.get_neighbors(v):
            if dls(neighbor, goal, limit - 1):
                return True

        return False
    
    return dls(start, goal, depth_limit)

def iterative_deepening_dfs(graph, start, goal):
    def dls(v, goal, limit):
        if v == goal:
            return True
        if limit <= 0:
            return False

        for neighbor in graph.get_neighbors(v):
            if dls(neighbor, goal, limit - 1):
                return True

        return False

    depth = 0
    while True:
        print(f"Depth Level {depth}")
        if dls(start, goal, depth):
            return True
        depth += 1

# Main function
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'F')
    g.add_edge('A', 'D')
    g.add_edge('A', 'E')
    g.add_edge('B', 'K')
    g.add_edge('B', 'J')
    g.add_edge('K', 'N')
    g.add_edge('K', 'M')
    g.add_edge('D', 'G')
    g.add_edge('E', 'C')
    g.add_edge('E', 'H')
    g.add_edge('I', 'L')

    # Depth-Limited Search
    start_node = 'A'
    goal_node = 'G'
    depth_limit = 3
    print(f"Starting Depth-Limited Search for goal {goal_node} with depth limit {depth_limit}")
    if depth_limited_search(g, start_node, goal_node, depth_limit):
        print(f"Goal node {goal_node} found within depth limit!")
    else:
        print(f"Goal node {goal_node} not found within depth limit.")

    # Iterative Deepening DFS
    print(f"\nStarting Iterative Deepening DFS for goal {goal_node}")
    if iterative_deepening_dfs(g, start_node, goal_node):
        print(f"Goal node {goal_node} found!")
    else:
        print(f"Goal node {goal_node} not found.")
