#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return None
        
        ls_1 = ListNode(-1)
        ls_2 = ListNode(-1)
        new_head = ls_1
        sec_head = ls_2
        cur = head
        
        while cur:
            if cur.val < x:
                ls_1.next = cur
                ls_1 = ls_1.next
            
            else:
                ls_2.next = cur
                ls_2 = ls_2.next
                
            cur = cur.next
        
        ls_1.next = sec_head.next
        ls_2.next = None
        
        return new_head.next

