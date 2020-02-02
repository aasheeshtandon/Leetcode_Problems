from __future__ import print_function

class EmptyQueueError(Exception):
    pass

class Queue:

    def __init__(self, dsize = 10):
        self.q = [None] * dsize
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, val):
        if len(self.q) == self.count:
            self.resize(2*len(self.q))
        else:
            i = (self.front + self.count) % len(self.q)
            self.q[i] = val
            self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty!")

        x = self.q[self.front]
        self.q[self.front] = None
        self.front = (self.front + 1) % len(self.q)
        self.count -= 1
        return x

    def resize(self, new_size):
        old_q = self.q
        self.q = [None] * new_size
        i = self.front
        for j in range(self.count):
            self.q[j] = old_q[i]
            i = (i+1) % len(old_q)
        self.front = 0

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
