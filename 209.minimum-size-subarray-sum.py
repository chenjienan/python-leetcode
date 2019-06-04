#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
                
        min_len = n+1
        cur_sum = 0
        left = 0
        for right in range(n):
            cur_sum += nums[right]
            
            # 若等于超过sum, 移动左指针，缩小len范围
            while cur_sum >= s:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
        return min_len if min_len != n+1 else 0

