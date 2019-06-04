#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        
        dummy = ListNode(-1)
        dummy.next = head

        right = dummy.next
        cnt = 0
        while cnt < n:            
            right = right.next
            cnt += 1

        # point to the node before head
        pre = dummy
        while right:
            pre = pre.next            
            right = right.next

        # skip the removed node
        pre.next = pre.next.next
        return dummy.next

