#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node'):
        
        if not root: return []
        
        import collections
        queue = collections.deque([root])
        res = []
        
        while queue:
            cur = queue.popleft()
            res.append(cur.val)
            
            if cur.children:
                children_ls = collections.deque(cur.children)
                queue = children_ls + queue
        
        return res
