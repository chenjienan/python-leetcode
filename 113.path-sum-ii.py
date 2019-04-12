#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (40.03%)
# Total Accepted:    222.2K
# Total Submissions: 555.1K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \    / \
# 7    2  5   1
# 
# 
# Return:
# 
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursion
# this problem is not that easy
# test case:
# 1. happy path: all positive number
# 2. nagative number
# 2.1 cur_sum goes up only
# 2.1 cur_sum goes up and down
class Solution:
    def pathSum(self, root, sum):
        if not root: return []
        self.res = []
        self.sum = sum
        
        self.dfs(root, root.val, [root.val])

        return self.res

    def dfs(self, node, cur_sum, cur_ls):        
        if not node.left and \
           not node.right and \
           cur_sum == self.sum:

           self.res.append(cur_ls)
            
        if node.left:
            self.dfs(node.left, cur_sum + node.left.val, cur_ls + [node.left.val])
        if node.right:
            self.dfs(node.right, cur_sum + node.right.val, cur_ls + [node.right.val])        

    # def dfs(self, node, cur_sum, cur_ls):
    #     if abs(cur_sum) > abs(self.sum): 
    #         return
    #     elif cur_sum == self.sum and not node.left and not node.right: 

    #         self.res.append(cur_ls)
    #         return
    #     if node.left:
    #         self.dfs(node.left, cur_sum + node.left.val, cur_ls + [node.left.val])
    #     if node.right:
    #         self.dfs(node.right, cur_sum + node.right.val, cur_ls + [node.right.val])
        
