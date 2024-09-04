class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def main():
    stack = Stack()
    print("Is stack empty?", stack.is_empty())
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushing 1, 2, 3:", stack.items)
    
    print("Peek top element:", stack.peek())
    
    print("Pop top element:", stack.pop())
    print("Stack after popping:", stack.items)
    
    print("Size of stack:", stack.size())
    print("Is stack empty?", stack.is_empty())

if __name__ == "__main__":
    main()