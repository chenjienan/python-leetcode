#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#
class Solution(object):
    def lengthOfLIS(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A: return 0

        dp = [1] * len(A)

        for i in range(1, len(A)):
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
            
        return max(dp)
