#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ptr = ListNode(-1)

        # need an auto-sort data structure: Heap
        heap = []
        # add all heads to the heap
        for head in lists:
            # * remember to push the value as a tuple 
            # in the heap so that the heap is min heap
            # need to check if list is empty....
            if head: heapq.heappush(heap, (head.val, head))

        while heap:
            _, cur_node = heapq.heappop(heap)
            ptr.next = cur_node
            ptr = ptr.next
            if cur_node.next:
                heapq.heappush(heap, (cur_node.next.val, cur_node.next))

        return dummy.next
