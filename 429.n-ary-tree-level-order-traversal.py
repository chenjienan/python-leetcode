#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node'):
        
        if not root: return []
        
        queue = [root]
        res = []
        
        while queue:
            res.append([node.val for node in queue])
            
            level = []
            for node in queue:
                level.extend(node.children)
            
            queue = level
        
        return res

