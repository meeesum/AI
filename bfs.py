from collections import deque
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def bfs(self, s):
        visited = [False] * self.V
        
        queue = deque()

        visited[s] = True
        queue.append(s)
        
        while queue:
            s = queue.popleft()
            print(s, end=' ')
            
            for i in self.adj[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
    
def bfs(graph, start_node):
    queue = deque([start_node])
    visited = set()

    traversal_order = []

    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)

            for neighbour in graph[current_node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return traversal_order
def bfs_with_Goal(graph, start_node, goal):
    queue = deque([start_node])
    
    visited = set()
    
    traversal_order = []
    
    while queue:
        current_node = queue.popleft()
        
        if current_node == goal:
            traversal_order.append(current_node)
            return traversal_order
        
        if current_node not in visited:
            visited.add(current_node)
            
            traversal_order.append(current_node)
            
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return traversal_order
if __name__ == "__main__":
    graph = {
        '0' : ['1', '4'],
        '1' : ['0', '2', '3', '4'],
        '2' : ['1', '3'],
        '3' : ['1', '2', '4'],
        '4' : ['0', '1', '3'],
    }
    graph2 = {
        'A' : ['B', 'F', 'D', 'E'],
        'I' : ['L'],
        'D' : ['G'],
        'B' : ['K', 'J'],
        'K' : ['N', 'M'],
        'E' : ['C', 'H', 'I'],
        'F' : [],
        'J' : [],
        'N' : [],
        'M' : [],
        'G' : [],
        'C' : [],
        'H' : [],
        'L' : []

    }

    # start_node = 'A'
    # print("BFS Traversal Order:", bfs(graph, '2'))
    print("Goal Search : ", bfs_with_Goal(graph2, 'A', 'G'))

    g = Graph(5)  # Create a graph with 5 vertices
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print("BFS Traversal starting from vertex 0:")
    g.bfs(0)