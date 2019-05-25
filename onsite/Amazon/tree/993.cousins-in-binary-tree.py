#
# @lc app=leetcode id=993 lang=python
#
# [993] Cousins in Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import collections
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root: return 

        queue = collections.deque([root])
        while queue:
            # level order traversal
            lv = []
            # all value are unique
            # key: node value
            # value: parent value
            d = {}
            for node in queue:
                if node.left: 
                    lv.append(node.left)
                    d[node.left.val] =  node.val
                if node.right: 
                    lv.append(node.right)
                    d[node.right.val] = node.val
            if x in d and y in d: 
                # cousin 不能又同一个parent
                return d[x] != d[y]
            
            queue = lv
        return False
