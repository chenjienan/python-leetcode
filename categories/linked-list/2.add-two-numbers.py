#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # list is reversed

        dummy = ptr = ListNode(-1)
        carry = 0
        while carry or l1 or l2:
            l1_val, l2_val = 0, 0

            if l1: 
                l1_val = l1.val
                l1 = l1.next
            if l2: 
                l2_val = l2.val
                l2 = l2.next
            
            new_val, carry = self.add(l1_val, l2_val, carry)
            new_node = ListNode(new_val)
            ptr.next = new_node
            ptr = ptr.next            
        
        return dummy.next

    def add(self, num1, num2, carry):
        res = num1 + num2 + carry
        return (res % 10, 1) if res > 9 else (res, 0)


