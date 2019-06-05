#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        
        curA, curB = headA, headB
        lenA, lenB = 0, 0

        # get the len of each list
        while curA:
            lenA +=1 
            curA = curA.next
        
        while curB:
            lenB += 1
            curB = curB.next
        
        if lenA > lenB:
            headA, headB = headB, headA         # headB is the longer one

        # # trim the longer list
        # # move pointers until they are the same node
        for _ in range(abs(lenA - lenB)):
            headB = headB.next
        
        # if no intersection, headA and headB will be None
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        
        # either headA or headB is ok
        return headB
