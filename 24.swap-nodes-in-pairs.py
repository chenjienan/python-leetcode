#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        cur = head
        while cur and cur.next:
            # ptr:     |
            # pre      cur
            # dummy -> 1-> 2-> 3-> 4-> none
            # ptr:             |
            # dummy -> 1-> 2-> 3-> 4-> none
            next_start_node = cur.next.next
            # pre => node 2
            pre.next = cur.next
            # next node of 2 (node 3) => node 1
            cur.next.next = cur
            # reset the current node (point to node 3)
            cur.next = next_start_node
            pre = cur
            cur = cur.next

        return dummy.next
        