#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

import math

class Solution:
    def numSquares(self, n: int):

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i-j**2] + 1)

        return dp[n]



# dp
# n = a^2 + b^2 + c^2 + x^2
# dp[n] = min { dp[n-x^2] + 1 } for all x