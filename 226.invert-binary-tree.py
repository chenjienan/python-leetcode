#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        
        import collections
        queue = collections.deque([root])

        while queue:
            cur_node = queue.popleft()

            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            if cur_node.left: queue.append(cur_node.left)        
            if cur_node.right: queue.append(cur_node.right)        
        
        return root
