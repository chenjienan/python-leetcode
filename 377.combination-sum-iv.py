#
# @lc app=leetcode id=377 lang=python
#
# [377] Combination Sum IV
#
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # keyword: all possible answer
        # 基本款DP (背包类?)
        # 同款: 322 coin change?

        #
        dp = [0] * (target+1)
        dp[0] = 1 # 什么都不选也是一种方案
        for i in range(1, target + 1):
            # update dp[i]
            for d in nums:
                if i >= d: dp[i] += dp[i-d]    # i - x 不可以 < 0
                
        return dp[target]

# dp[i] 通过手头的面值
# 求dp[4] target = 4



