#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        # need dummy node for head reference
        # because the linkedlist changed after reversed.
        new_head = ListNode(-1)
        new_head.next = head        # append the list
        
        pre = new_head
        for _ in range(1, m):
            pre = pre.next

        start = pre.next
        nxt = start.next

        for _ in range(m, n):
            start.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
            nxt = start.next

        return new_head.next
   