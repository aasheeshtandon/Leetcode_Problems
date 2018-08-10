# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrderHelper(self, root):
        if root is None:
            return
        self.inOrderHelper(root.left)
        self.result.append(root.val)
        self.inOrderHelper(root.right)
        
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.inOrderHelper(root)
        return self.result
    
