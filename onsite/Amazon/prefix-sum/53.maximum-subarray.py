#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = 0
        min_sum = 0
        max_sum = nums[0]   # or -float('inf')

        # 计算每个位置为结尾的 subarray 的最大值是多少
        for d in nums:
            prefix_sum += d
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum
        

