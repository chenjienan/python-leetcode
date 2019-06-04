#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:        
        if head == None or head.next == None: return True

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        rev_sec_half = self.reverse_list(slow.next)
        slow.next = None
        
        while rev_sec_half:
            if head.val != rev_sec_half.val:
                return False
            head = head.next
            rev_sec_half = rev_sec_half.next
        
        return True
            
    def reverse_list(self, head):

        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre
