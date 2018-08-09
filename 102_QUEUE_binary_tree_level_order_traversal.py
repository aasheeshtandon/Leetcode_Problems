# Level Order Traversal Queue Method
## Time Complexity: O(n) where n is number of nodes in the binary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printLevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].val, end=" ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


# Driver Program
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(10)
    root.right.left = Node(8)
    printLevelOrder(root)

