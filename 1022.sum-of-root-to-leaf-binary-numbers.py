#
# @lc app=leetcode id=1022 lang=python
#
# [1022] Sum of Root To Leaf Binary Numbers
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        self.res = 0
        self.dfs(root, str(root.val))
        return self.res

    def dfs(self, node, cur_str):
        if not node.left and not node.right:
            self.res += int(cur_str, 2)
            return 
        
        if node.left: self.dfs(node.left, cur_str + str(node.left.val))
        if node.right: self.dfs(node.right, cur_str + str(node.right.val))

