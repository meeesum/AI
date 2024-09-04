import math

# Define the structure of a game node
class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children is not None else []

# Define utility functions
def is_terminal(node):
    # A node is terminal if it has no children
    return len(node.children) == 0

def evaluate(node):
    # Return the value of the node
    return node.value

def get_children(node):
    # Return the list of children nodes
    return node.children

def minimax(node, depth, maximizingPlayer):
    if depth == 0 or is_terminal(node):
        return evaluate(node)
    
    if maximizingPlayer:
        maxEval = -math.inf
        for child in get_children(node):
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = math.inf
        for child in get_children(node):
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval

# Example usage
if __name__ == "__main__":
    # Constructing the game tree based on the example in the document

    # Terminal nodes
    D = Node(value=4)
    E = Node(value=6)
    F = Node(value=-3)
    G = Node(value=7)

    # Second level
    B = Node(children=[D, E])
    C = Node(children=[F, G])

    # Root node
    A = Node(children=[B, C])

    # Initial call to minimax
    best_value = minimax(A, depth=3, maximizingPlayer=True)
    print("Best value for maximizer:", best_value)  # Output should be 4
