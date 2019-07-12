#
# @lc app=leetcode id=545 lang=python
#
# [545] Boundary of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        if not root.left and not root.right: return [root.val]

        left_boundary = self.find_left_boundary(root.left)
        leaves = collections.deque(self.find_leaves(root))
        right_boundary = self.find_right_boundary(root.right)
        if left_boundary and leaves and leaves[0] == left_boundary[-1]: leaves.popleft()
        if right_boundary and leaves and leaves[-1] == right_boundary[-1]: leaves.pop()
        return [root.val] + left_boundary + list(leaves) + list(reversed(right_boundary))
    
    # # bfs
    # def find_right_boundary(self, root):
    #     right_bound = []
    #     if not root: return right_bound

    #     queue = [root]
    #     while queue:
    #         if not self.is_leaf(queue[-1]):
    #             right_bound.append(queue[-1].val)
    #         lv = []
    #         for node in queue:
    #             if node.left: lv.append(node.left)
    #             if node.right: lv.append(node.right)            
    #         queue = lv
    #     return right_bound
    
    # # bfs
    # def find_left_boundary(self, root):
    #     left_bound = []
    #     if not root: return left_bound
    
    #     queue = [root]
    #     while queue:
    #         if not self.is_leaf(queue[0]):
    #             left_bound.append(queue[0].val)
    #         lv = []
    #         for node in queue:
    #             if node.left: lv.append(node.left)
    #             if node.right: lv.append(node.right)            
    #         queue = lv
    #     return left_bound

    def find_left_boundary(self, node):
        left_boundary = []
        while node:
            left_boundary.append(node.val)
            if node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                break
        return left_boundary

    def find_right_boundary(self, node):
        right_boundary = []
        while node:
            right_boundary.append(node.val)
            if node.right:
                node = node.right
            elif node.left:
                node = node.left
            else:
                break
        return right_boundary

    # dfs
    def find_leaves(self, root):
        stack = [root]
        leaves = []
        while stack:
            node = stack.pop()
            if self.is_leaf(node):
                leaves.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return leaves
    
    def is_leaf(self, node):
        return not node.left and not node.right
