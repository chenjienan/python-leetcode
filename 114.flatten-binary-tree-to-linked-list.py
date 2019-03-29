#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (41.49%)
# Total Accepted:    225.6K
# Total Submissions: 543.6K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return 
        
        stack = [root]      # maintain a record of the next "root"
        while stack:
            node = stack.pop()

            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

            node.left = None        # clear left node

            # set left node
            if stack: node.right = stack[-1]
            else: node.right = None



#     1                1                    1 
#   2  5      =>   None  2 (node)    => None  2
#  3 4   6              3  4                    3
#                  stack = [5]

