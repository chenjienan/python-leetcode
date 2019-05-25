#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for d in nums:
            heapq.heappush(heap, -d)

        res = None
        for _ in range(k):
            res = heapq.heappop(heap)

        return -res
