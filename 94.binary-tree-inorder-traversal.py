#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (55.28%)
# Total Accepted:    418.2K
# Total Submissions: 756.5K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []

        # self.traverse(root, res)
        # return res

        if not root: return []

        res, s = [], []
        node = root
        while node or s:
            while node:     # traverse each node's left node until leaf is reached
                s.append(node)
                node = node.left
            node = s.pop()      # grab relative "root"
            res.append(node.val)    
            node = node.right   # grab right node        

        return res

    def traverse(self, node, res):
        if not node: return
        
        self.traverse(node.left, res)
        res.append(node.val)
        self.traverse(node.right, res)

