#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
# key: old node
# value: new node
visited = {}
class Solution(object):

    
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return head
        
        if head in visited: return visited[head]
        
        node = Node(head.val, None, None)
        visited[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node

