#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        # num of distinct subsequences of S[:i] which equals T[:j].
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # we have one sub-seq if j is empty
        for k in range(m+1):
            dp[k][0] = 1                

        for i in range(1, m+1):
            for j in range(1, n+1):
                # transition function
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
                
                dp[i][j] += dp[i-1][j]
                
        return dp[m][n]