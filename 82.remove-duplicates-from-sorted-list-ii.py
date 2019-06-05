#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        
        
        pre = dummy     # avoid the head is a duplication
        cur = head
        
        while cur and cur.next:
            
            if cur.val == cur.next.val:
                val = cur.val
                while cur and val == cur.val:
                    cur = cur.next
                pre.next = cur                
            else:
                pre = pre.next
                cur = cur.next
                
        return dummy.next

