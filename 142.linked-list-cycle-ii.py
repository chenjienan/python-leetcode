#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 假设环的长度为l，环上入口距离链表头距离为a，两指针第一次相遇处距离环入口为b，
        # 则另一段环的长度为c=l-b，由于快指针走过的距离是慢指针的两倍，则有a+l+b=2*(a+b),
        # 又有l=b+c，可得a=c
        slow, fast = head, head
        target = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:               
                while target != slow: 
                   target = target.next
                   slow = slow.next
                
                return target
                   
        return None

