# Constants representing infinity
INFINITY = float('inf')

# Node class definition
class Node:
    def __init__(self, value=None, children=None):
        self.value = value  # The value of the node (only for leaf nodes)
        self.children = children or []  # List of child nodes

# Function to implement minimax algorithm with alpha-beta pruning
def minimax(node, depth, isMaximizingPlayer, alpha, beta):
    # Base case: if the node is a leaf node, return its evaluated value (numeric)
    if is_leaf_node(node):
        return evaluate_node(node)
    
    if isMaximizingPlayer:
        bestVal = -INFINITY
        for child in get_children(node):
            value = minimax(child, depth + 1, False, alpha, beta)
            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            
            # Prune the branch
            if beta <= alpha:
                break
        return bestVal
    else:
        bestVal = INFINITY
        for child in get_children(node):
            value = minimax(child, depth + 1, True, alpha, beta)
            bestVal = min(bestVal, value)
            beta = min(beta, bestVal)
            
            # Prune the branch
            if beta <= alpha:
                break
        return bestVal

# Helper functions
def is_leaf_node(node):
    return len(get_children(node)) == 0

def evaluate_node(node):
    return node.value

def get_children(node):
    return node.children

# Main function
if __name__ == "__main__":
    # Create the tree structure from the example
    leaf_D = [Node(3), Node(5)]
    leaf_E = [Node(6)]  # Second child of E is pruned, so it's not explored
    leaf_F = [Node(1), Node(2)]
    leaf_G = [Node(0), Node(-1)]  # This part is pruned and not explored

    D = Node(children=leaf_D)
    E = Node(children=leaf_E)
    F = Node(children=leaf_F)
    G = Node(children=leaf_G)

    B = Node(children=[D, E])
    C = Node(children=[F, G])

    A = Node(children=[B, C])

    # Call the minimax function on the root node
    optimal_value = minimax(A, 0, True, -INFINITY, INFINITY)
    print(f"The optimal value is: {optimal_value}")
