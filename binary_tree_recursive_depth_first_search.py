# Depth first search for binary tree
## Time complexity: O(n)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printPreorder(root):
    if root is None:
        return

    print(root.val, end=" ")
    printPreorder(root.left)
    printPreorder(root.right)


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)


def printPostorder(root):
    if root is None:
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.val, end=" ")

# Driver method
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Preorder traversal of binary tree is")
    printPreorder(root)

    print("\nInorder traversal of binary tree is")
    printInorder(root)

    print("\nPostorder traversal of binary tree is")
    printPostorder(root)
