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
        
        # trim the longer list
        curA, curB = headA, headB
        for _ in range(abs(lenA-lenB)):
            if lenA >= lenB: curA = curA.next
            else: curB = curB.next
        
        # move pointers until they are the same node
        # if no intersection, curA and curB will be None
        while curB != curA:
            curA = curA.next
            curB = curB.next

        # either curA or curB is ok
        return curB
