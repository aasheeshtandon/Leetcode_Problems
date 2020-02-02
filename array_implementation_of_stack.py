class Stack():

    def __init__(self, maxsize = 10):
        self.items = [None] * maxsize
        self.count = 0

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def push(self, x):
        if self.count == len(self.items):
            print("Stack is full")
            return
        self.items[self.count] = x
        self.count += 1

    def pop(self):
        if self.count == 0:
            print("Stack is Empty")
            return
        x = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count -= 1
        return x

    def size(self):
        return len(self.count)

    def isFull(self):
        if len(self.items) == self.count:
            return True
        else:
            return False

    def top(self):
        if self.count == 0:
            print("Stack is Empty")
            return
        return self.items[self.count-1]

    def display(self):
        print("The Stack is: ",(self.items))

def main():
    s = Stack(7)
    print(s.isEmpty())
    print(s.display())
    s.push(31)
    s.push(42)
    s.push(53)
    s.push(64)
    s.push(75)
    print(s.isEmpty())
    print(s.isFull())
    print(s.display())
    print("item deleted is", s.pop())
    print(s.display())
    print("item deleted is",s.pop())
    print("item deleted is",s.pop())
    print(s.display())
    print(s.items)

if __name__=='__main__':
    main()
