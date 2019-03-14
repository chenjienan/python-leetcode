#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (50.40%)
# Total Accepted:    310.4K
# Total Submissions: 615.8K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,2,3]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        # res = []
        # self.traverse(root, res)
        # return res


        # TODO:Iteration
        # time: O(n)
        # space: O(h)
        if not root: return []
                
        s = [root]  # put root to init the stack
        res = []
        while s:
            node = s.pop()
            if node:
                # root -> left -> right
                res.append(node.val)
                s.append(node.right)    # use stack, so put right node first
                s.append(node.left)     # then left node
        return res

    # TODO: recursion: 
    # time: O(n)
    # space: O(1)
    def traverse(self, node, res):
        if not node: return
        
        res.append(node.val)
        self.traverse(node.left, res)        
        self.traverse(node.right, res)
