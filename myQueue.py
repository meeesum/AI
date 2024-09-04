class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def main():
    queue = Queue()
    print("Is queue empty?", queue.is_empty())
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue after enqueuing 1, 2, 3:", queue.items)
    
    print("Peek front element:", queue.peek())
    
    print("Dequeue front element:", queue.dequeue())
    print("Queue after dequeuing:", queue.items)
    
    print("Size of queue:", queue.size())
    print("Is queue empty?", queue.is_empty())

if __name__ == "__main__":
    main()