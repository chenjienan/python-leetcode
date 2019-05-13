#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # if not root: return True
        
        # # bfs        
        # # (cur_node, lower_bound, upper_bound)
        # queue = deque([(root, -float('inf'), float('inf'))])
        # while queue:           
        #     cur_node, lower_bound, upper_bound = queue.popleft()

        #     if cur_node.left:
        #         if cur_node.left.val >= cur_node.val or cur_node.left.val <= lower_bound: return False
        #         queue.append((cur_node.left, lower_bound, cur_node.val))            

        #     if cur_node.right:
        #         if cur_node.right.val <= cur_node.val or upper_bound <= cur_node.right.val: return False
        #         queue.append((cur_node.right, cur_node.val, upper_bound))       

        # return True  

        return self.dfs(root, -float('inf'), float('inf'))

    def dfs(self, node, lower_bound, upper_bound):
        if not node: return True
        if node.val >= upper_bound or node.val <= lower_bound: return False
        
        left = self.dfs(node.left, lower_bound, node.val)
        right = self.dfs(node.right, node.val, upper_bound)

        return left and right

