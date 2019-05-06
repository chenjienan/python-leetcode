#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        # i: dealt with substr [:i] of word1    
        # j: dealt with substr [:j] of word2
        # dp[i][j]: the min step required to make the word1[:i] and word2[:j] the same
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]

        # init
        for k in range(n+1):
            dp[0][k] = k
        
        for k in range(m+1):
            dp[k][0] = k

        for i in range(1, m+1):
            for j in range(1, n+1):
                # increment dp by 1
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
                # dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                # dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        
        return dp[m][n]

# # dp[i][j]
# # 甩锅给子问题
# # dp[i-1][j-1]
# if word1[i] == word2[j]:
#     dp[i][j] = min(dp[i][j], dp[i-1][j-1])

# # dp[i-1][j]
# dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)

# # dp[i][j-1]
# dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)