#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dfs
        self.count = 0

        self.dfs(root)
        return self.count
        
    def dfs(self, node):
        if not node: return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.count = max(self.count, left + right)
        return max(left, right) + 1