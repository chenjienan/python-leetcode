#
# @lc app=leetcode id=863 lang=python
#
# [863] All Nodes Distance K in Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # dfs where we annotate 
        # every node with information about it's parent
        def dfs(node, parent = None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        # bfs start from the target nodeto find all nodes
        # a distance K from the target
        queue = collections.deque([(target, 0)])    # (node, distance)
        visited = {target}
        while queue:
            # found the K distance
            if queue[0][1] == K: return [node.val for (node, dist) in queue]
            
            node, dist = queue.popleft()
            # child nodes and parent nodes can be neighbours
            for neighbour in (node.left, node.right, node.parent):
                if neighbour and neighbour not in visited:
                    queue.append((neighbour, dist + 1))
                    visited.add(neighbour)

        return []

