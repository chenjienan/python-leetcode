#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []

        # level order traversal and take the last item
        res = []
        queue = [root]
        while queue:
            
            level = []
            res.append(queue[-1].val)
            for node in queue:
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            
            queue = level

        return res

