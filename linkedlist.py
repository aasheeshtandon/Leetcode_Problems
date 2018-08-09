# Class for a node
class Node:
    # Method to initialize a node object.
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Method to initialize a node object
    def __init__(self):
        self.head = None

    # Inserts a new node at the beginning.
    def insertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    # Inserts a new node after the given prev_node value.
    def insertAfter(self, value, data):
        temp = self.head
        newNode = Node(data)
        while temp:
            if temp.data == value:
                break
            else:
                temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

    # Inserts a new node at the end of the last list.
    def append(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    # Method to delete a node of given value.
    def deletenode(self, value):
        temp = self.head
        if temp.data == value:
            self.head = temp.next
            return
        prev = None
        while temp:
            if temp.data == value:
                prev.next = temp.next
                return
            else:
                prev = temp
                temp = temp.next
        print("Value not found in the list!")

    # Method to print the linkedlist.
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()


# Driver code to test the functionality of the above methods.
if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBegin(5)
    ll.insertAtBegin(10)
    ll.insertAtBegin(15)
    ll.printList()
    ll.insertAfter(5, 20)
    ll.printList()
    ll.append(55)
    ll.insertAtBegin(1)
    ll.printList()
    ll.deletenode(1)
    ll.printList()

