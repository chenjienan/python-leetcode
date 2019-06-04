#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        
        cur = head
        insert_pos = dummy
        
        while cur and cur.next:
            next_val = cur.next.val
            
            if cur.val <= next_val:
                cur = cur.next
                continue
            
            if insert_pos.next.val > next_val:
                insert_pos = dummy                  # reset
            
            # use the insert position
            while insert_pos.next.val < next_val:
                insert_pos = insert_pos.next        # move pos pointer
                
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = insert_pos.next
            insert_pos.next = nxt
            
        return dummy.next


