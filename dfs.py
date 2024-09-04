class Graph:
    def __init__(self, V):
        # Number of vertices
        self.V = V
        # Adjacency list representation of the graph
        self.adj = [[] for _ in range(V)]

    # Add an edge to the graph
    def add_edge(self, v, w):
        self.adj[v].append(w)

    # Iterative DFS using a stack (no recursion)
    def dfs(self, start_vertex):
        # Create a stack for DFS
        stack = []
        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Push the starting vertex to the stack
        stack.append(start_vertex)

        while stack:
            # Pop a vertex from the stack
            vertex = stack.pop()

            # If this vertex hasn't been visited yet
            if not visited[vertex]:
                # Mark it as visited and print it
                print(vertex, end=' ')
                visited[vertex] = True

            # Get all adjacent vertices of the popped vertex
            # If an adjacent vertex hasn't been visited, push it to the stack
            for neighbor in reversed(self.adj[vertex]):
                if not visited[neighbor]:
                    stack.append(neighbor)

# Main function
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    # Perform DFS traversal starting from vertex 0
    print("DFS Traversal starting from vertex 0:")
    g.dfs(0)
