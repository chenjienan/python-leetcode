#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        
        for i in range(1, len(s) + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]    # follow the previous one
            
            if i >= 2 and (s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '7')):
                dp[i] += dp[i-2]
        
        return dp[-1]
            

