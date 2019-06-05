#
# @lc app=leetcode id=700 lang=python
#
# [700] Search in a Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        cur_node = root
        while cur_node:
            if cur_node.val == val:
                return cur_node
            elif cur_node.val < val:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left

