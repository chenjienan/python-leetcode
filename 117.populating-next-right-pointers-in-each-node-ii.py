#
# @lc app=leetcode id=117 lang=python
#
# [117] Populating Next Right Pointers in Each Node II
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return 
        # connect nodes level by level,
        # similar to level order traversal
        queue = collections.deque([root])
        nextLevel = collections.deque([])

        while queue:
            node = queue.popleft()
            if node.left: nextLevel.append(node.left)
            if node.right: nextLevel.append(node.right)
                
            # at the same level, cur_node always points to 
            # the first element of the queue
            if queue: node.next = queue[0]
            else: queue, nextLevel = nextLevel, queue  
        
        return root

