#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # ensure p is < q
        if p.val > q.val:
            p, q = q, p

        if p.val <= root.val and q.val >= root.val:
            return root

        # divide and conquer 
        # if target is in left subtree
        elif q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # target is in right subtree
        else:
            return self.lowestCommonAncestor(root.right, p, q)
