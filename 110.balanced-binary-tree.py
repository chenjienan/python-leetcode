#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        height = self.get_height(root)
        return height != -1

    def get_height(self, node):
        if not node: return 0

        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        if abs(left_height - right_height) > 1 or \
           left_height == -1 or \
           right_height == -1:
           return -1

        return max(left_height, right_height) + 1

