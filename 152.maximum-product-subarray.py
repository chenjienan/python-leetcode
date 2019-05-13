#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums: return

        global_max = pre_max = pre_min = nums[0]

        for d in nums[1:]:
            if d > 0:
                local_max = max(d, pre_max * d)
                local_min = min(d, pre_min * d)
            else:
                local_max = max(d, pre_min * d)
                local_min = min(d, pre_max * d)
            
            pre_max = local_max
            pre_min = local_min

            global_max = max(global_max, local_max)

        return global_max

