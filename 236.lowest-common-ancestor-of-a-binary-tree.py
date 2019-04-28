#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        stack = [root]

        # key: node, value: parent_node
        parent = {root: None}

        # get the parent of q and p
        while q not in parent or p not in parent:
            cur_node = stack.pop()
            if cur_node.left:
                parent[cur_node.left] = cur_node
                stack.append(cur_node.left)

            if cur_node.right:
                parent[cur_node.right] = cur_node
                stack.append(cur_node.right)    

        # collect all ancestors of p
        p_ancestors = set()   
        while p:
            p_ancestors.add(p)
            p = parent[p]

        # find the first ancestor of q in p_ancestors
        while q not in p_ancestors:
            q = parent[q]

        # q is the LCA
        return q

