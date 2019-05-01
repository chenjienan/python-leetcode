#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range
#
import heapq

class Solution:
    def smallestRange(self, nums):
        heap = []

        for i, v in enumerate(nums):
            if len(v) == 0: continue
            heapq.heappush(heap, (v[0], i, 0))

        min_range = [-float('inf'), float('inf')]
        cur_max = max(heap)[0]

        while len(heap) == len(nums):
            cur_min, array_i, elem_i = heapq.heappop(heap)
            
            if cur_max - cur_min < min_range[1] - min_range[0]:
                min_range = [cur_min, cur_max]

            if elem_i < len(nums[array_i]) - 1:
                cur_max = max(cur_max, nums[array_i][elem_i+1])
                heapq.heappush(heap, (nums[array_i][elem_i+1], array_i, elem_i + 1))
                
        return min_range


# s = Solution()
# # s.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
# print(s.smallestRange([[10,10],[11,11]]))
