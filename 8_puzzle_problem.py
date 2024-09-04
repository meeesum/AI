import heapq

class Node:
    def __init__(self, state, parent=None, move=None, g_cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost  # Cost to reach this node
        self.h_cost = self.misplaced_tiles()  # Heuristic cost (number of misplaced tiles)
        self.f_cost = g_cost + self.h_cost  # Total cost (g_cost + h_cost)

    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def misplaced_tiles(self):
        goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        misplaced = sum(1 for i in range(9) if self.state[i] != goal_state[i] and self.state[i] != 0)
        return misplaced

    def get_neighbors(self):
        neighbors = []
        index = self.state.index(0)
        x, y = divmod(index, 3)

        def swap_and_create_new_state(x1, y1, x2, y2):
            new_state = self.state[:]
            idx1 = x1 * 3 + y1
            idx2 = x2 * 3 + y2
            new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
            return new_state

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = swap_and_create_new_state(x, y, new_x, new_y)
                neighbors.append(Node(new_state, self, (new_x, new_y), self.g_cost + 1))
        
        return neighbors

def a_star_search(start_state, goal_state):
    start_node = Node(start_state)
    goal_node = Node(goal_state)
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)
    closed_list.add(tuple(start_state))

    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.state == goal_node.state:
            return reconstruct_path(current_node)
        
        for neighbor in current_node.get_neighbors():
            if tuple(neighbor.state) in closed_list:
                continue
            
            closed_list.add(tuple(neighbor.state))
            heapq.heappush(open_list, neighbor)
    
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

# Example usage
start_state = [1, 2, 3, 5, 6, 0, 7, 8 , 4]
goal_state = [1, 2, 3, 5, 8, 6, 0, 7, 4]

path = a_star_search(start_state, goal_state)
if path:
    for step in path:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution found")
