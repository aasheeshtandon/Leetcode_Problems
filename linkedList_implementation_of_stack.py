from __future__ import print_function

class Node:

    def __init__(self,value):
        self.val = value
        self.next = None

class Stack():

    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, x):
        temp = Node(x)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.isEmpty():
            print("Stack is already empty!")
            return
        popped = self.top.val
        self.top = self.top.next
        return popped

    def size(self):
        counter = 0
        p = self.top
        while p is not None:
            counter += 1
            p = p.next
        return counter

    def top(self):
        if self.isEmpty():
            print("Stack is empty!")
            return
        else:
            return self.top.val

    def display(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            p = self.top
            while p is not None:
                print(p.val," ",end='')
                p = p.next

def main():
    s = Stack()
    print(s.isEmpty())
    print(s.display())
    s.push(31)
    s.push(42)
    s.push(53)
    s.push(64)
    s.push(75)
    print(s.isEmpty())
    print(s.display())
    print("Item deleted is", s.pop())
    print(s.display())
    print("Item deleted is",s.pop())
    print("Item deleted is",s.pop())
    print(s.display())

if __name__=='__main__':
    main()

