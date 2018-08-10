# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preOrderHelper(self, root):
        if root is None:
            return
        self.result.append(root.val)
        self.preOrderHelper(root.left)
        self.preOrderHelper(root.right)
        
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.preOrderHelper(root)
        return self.result
        
        
