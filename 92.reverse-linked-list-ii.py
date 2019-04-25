#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        new_head = ListNode(-1)
        new_head.next = head        # 0 -> X -> Y -> Z -> ....

        cur, pre = head, new_head
        print(cur.val, pre.val)
        for _ in range(1, m):
            cur = cur.next
            pre = pre.next

        print(cur.val, pre.val)
        # reverse sublist
        for _ in range(n - m):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        
        return new_head.next
            
