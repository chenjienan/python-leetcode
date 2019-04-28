#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        # here is the trick:
        # keep a stack of pairs         
        stack = [(root.left, root.right)]

        while stack:
            # pop one pair and compare
            left, right = stack.pop()

            # reach leaf
            if not left and not right: continue
            
            if (not left and right) or \
                (left and not right) or \
                (left.val != right.val):
                return False

            # add next pairs iteratively
            stack.append((left.right, right.left))
            stack.append((left.left, right.right))
        
        return True
