from __future__ import print_function

class EmptyQueueError(Exception):
    pass

class Queue:

    def __init__(self):
        self.q = []
        self.front = 0

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return (len(self.q) - self.front)

    def enqueue(self, val):
        self.q.append(val)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty!")

        x = self.q[self.front]
        self.q[self.front] = None
        self.front += 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty!")
        return self.q[self.front]

    def display(self):
        print(self.q)

def main():
    i = Queue()
    i.enqueue(12)
    i.enqueue(16)
    i.enqueue(20)
    i.enqueue(24)
    i.enqueue(26)
    i.enqueue(28)
    i.display()
    print("Size of queue is: ",i.size())
    x = i.dequeue()
    print("Item deleted is: ", x)
    i.display()
    x = i.dequeue()
    print("Item deleted is: ", x)
    i.display()
    x = i.dequeue()
    print("Item deleted is: ", x)
    i.display()
    print("Currently front is at: ", i.peek())
    print("Size of queue is: ", i.size())
    i.enqueue(32)
    i.enqueue(36)
    i.display()
    x = i.dequeue()
    print("Item deleted is: ", x)
    i.display()
    print("Currently front is at: ", i.peek())
    print("Size of queue is: ", i.size())


if __name__ == '__main__':
    main()
