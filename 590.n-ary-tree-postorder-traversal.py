#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node'):
        
        if not root: return []
        
        stack = [root]
        res = []
        
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            
            if cur.children:
                stack.extend(cur.children)
            
        return res[::-1]
