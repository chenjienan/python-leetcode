#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)        
        dp = [[False] * (n+1) for _ in range(m+1)]

        # padding char in the strings so that the 
        # indices can match the one in dp function
        s = '#' + s
        p = '#' + p

        # init
        dp[0][0] = True

        # when s is empty
        for j in range(2, n + 1):
            dp[0][j] = p[j] == '*' and dp[0][j-2]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j].isalpha():
                    dp[i][j] = dp[i-1][j-1] and s[i] == p[j]

                elif p[j] == '.':
                    dp[i][j] = dp[i-1][j-1]

                elif p[j] == '*':
                    # when star combo is skipped (zero)
                    candidate1 = dp[i][j-2]
                    # when star combo contains many preceding element (more)
                    # or preceding element is wildcard
                    candidate2 = dp[i-1][j] and (s[i] == p[j-1] or p[j-1] == '.')                    
                    dp[i][j] = candidate1 or candidate2

        return dp[m][n]
