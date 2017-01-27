# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        
    def dfs(self, node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if (left!=None): self.dfs(left)
        if (right!=None): self.dfs(right)