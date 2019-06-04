#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return 
        if not head.next: return head
        
        dummy = ListNode(-1)
        dummy.next = head
        
        # get the size of the list
        # k % list size
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
        
        steps = k % cnt
        if steps == 0: return head
        
        # 快慢指针get the kth last node
        # get the very last node
        right = dummy.next  # set to head
        cnt = 0
        while cnt < steps:
            right = right.next
            cnt += 1
            
        pre_kth_node = dummy
        
        while right:
            pre_kth_node = pre_kth_node.next
            right = right.next
        
        new_head = pre_kth_node.next
        pre_kth_node.next = None
        
        connector = new_head
        while steps > 1:
            connector = connector.next
            steps -= 1
            
        connector.next = dummy.next
        
        return new_head

