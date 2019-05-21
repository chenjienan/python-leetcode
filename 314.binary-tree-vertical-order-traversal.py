#
# @lc app=leetcode id=314 lang=python
#
# [314] Binary Tree Vertical Order Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # 解题关键: BFS + hashtable
        # 使用defaultdict 可以随时append,不用担心为空
        hash = collections.defaultdict(list)
        # (node, postition)
        queue = collections.deque([(root, 0)])

        while queue:
            node, pos = queue.popleft() 
            if node:
                hash[pos].append(node.val)
                queue.append((node.left, pos - 1))
                queue.append((node.right, pos + 1))
        
        # 按照key排序
        return [hash[i] for i in sorted(hash)]
        

