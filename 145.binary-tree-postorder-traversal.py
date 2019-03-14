#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (47.11%)
# Total Accepted:    239.9K
# Total Submissions: 509.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [3,2,1]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # self.traverse(root, res)

        # return res

        # using a flag to indicate whether the node has been visited or not
        res, s = [], [(root, False)]
        while s:
            node, visited = s.pop()

            if node:
                if visited:
                    res.append(node.val)
                else:
                    # stack: add node -> right - left
                    # when pop: left -> right -> node
                    s.append((node, True))
                    s.append((node.right, False))
                    s.append((node.left, False))
        return res


    def traverse(self, node, res):
        if not node: return 
                
        self.traverse(node.left, res)
        self.traverse(node.right, res)
        res.append(node.val)

