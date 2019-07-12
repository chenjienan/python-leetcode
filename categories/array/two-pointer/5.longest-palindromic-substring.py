# collected
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.88%)
# Total Accepted:    513.7K
# Total Submissions: 1.9M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        
        res = ''
        
        # from left to right
        for i in range(len(s)):
            odd  = self.helper(s, i, i) 
            even = self.helper(s, i, i+1)

            res = max(res, odd, even, key=len)
        
        return res
    
    # from middle to two ends
    def helper(self, s, l, r):
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l+1: r]

