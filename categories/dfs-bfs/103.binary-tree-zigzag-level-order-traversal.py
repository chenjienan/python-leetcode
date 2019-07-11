#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root: return []
        
        queue = [root]
        res = []
        is_reversed = False
        while queue:
            level_node_val = [node.val for node in queue]
            if is_reversed: 
                level_node_val.reverse()
                is_reversed = False
            else:
                is_reversed = True
            res.append(level_node_val)

            level = []
            for cur_node in queue:                     
                if cur_node.left: level.append(cur_node.left)
                if cur_node.right: level.append(cur_node.right)
            
            queue = level

        return res
            
