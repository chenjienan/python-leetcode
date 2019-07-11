#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.max_sum = -float('inf')

        self.helper(root)
        return self.max_sum

    def helper(self, node):
        if not node: return 0

        left_sum = self.helper(node.left)
        right_sum = self.helper(node.right)
        # find max
        self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
        # 分治到底部，在返回的时候传入左右任意一遍最大值加上目前node.val
        cur_max = max(left_sum, right_sum) + node.val
        # 对于最底部叶子节点传上来的值，我们将其设置成0
        # a path is defined as any sequence of nodes 
        # from some starting node to any node in the 
        # tree along the parent-child connections

        # 对parent tree 无贡献,设置为0
        return cur_max if cur_max > 0 else 0

