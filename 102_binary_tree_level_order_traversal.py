
# Recursive Level Order Traversal of a Binary Tree.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def printLevelOrder(root):
    if root is None:
        return
    h = height(root)
    for i in range(1, h + 1):
        printCurrentLevel(root, i)

def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)

# Driver Program to test the above methods.
if __name__ == '__main__':
    root = Node(3)
    root.left = Node(1)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(2)
    root.right.left = Node(6)
    # Calling the Level Order Traversal Method.
    printLevelOrder(root)

