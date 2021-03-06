#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (34.82%)
# Total Accepted:    319.7K
# Total Submissions: 918K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP solution
        # n = len(s)
        # dp = [True] + [False] * (n)
        # # i limit the length of the word
        # for i in range(n+1):
        #     for k in range(i):
        #         # [0 - k] 有解
        #         if dp[k] and s[k:i] in wordDict: 
        #             dp[i] = True
        #             break
        # return dp[n] 

        # DFS + memo
        wordDict = set(wordDict)
        return self.canBreak(s, wordDict, {})
    
    
    # memo stores boolean if [0:index] is breakable
    # and memo is a dictionary
    def canBreak(self, s, wordDict, memo):
        if s in memo: return memo[s]
        
        if s in wordDict: 
            memo[s] = True
            return True

        for i in range(len(s)):
            left = s[:i]
            right = s[i:]
            if right in wordDict and self.canBreak(left, wordDict, memo):
                memo[s] = True
                return True

        memo[s] = False
        return False 

