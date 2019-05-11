#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 1: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums)

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]
s = Solution()
# s.rob([2, 7, 9, 3,1])
s.rob([1,2,3,1])