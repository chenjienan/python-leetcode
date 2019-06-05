#
# @lc app=leetcode id=328 lang=python
#
# [328] Odd Even Linked List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even_dummy_head = ListNode(-1)
        odd_dummy_head = ListNode(-1)

        # pointers
        even_ptr = even_dummy_head
        odd_ptr = odd_dummy_head
        i = 1
        while head:
            # 交错地连接
            if i % 2:
                odd_ptr.next = head
                odd_ptr = head
            else:
                even_ptr.next = head
                even_ptr = head
            
            head = head.next
            i += 1
        
        # 尾部处理
        odd_ptr.next = even_dummy_head.next
        even_ptr.next = None

        return odd_dummy_head.next

