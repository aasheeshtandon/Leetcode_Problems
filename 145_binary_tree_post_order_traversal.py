# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postOrderHelper(self, root):
        if root is None:
            return
        self.postOrderHelper(root.left)
        self.postOrderHelper(root.right)
        self.result.append(root.val)
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.postOrderHelper(root)
        return self.result
