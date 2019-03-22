#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (55.52%)
# Total Accepted:    39.9K
# Total Submissions: 71.8K
# Testcase Example:  '"a1b2"'
#
# Given a string S, we can transform every letter individually to be lowercase
# or uppercase to create another string.  Return a list of all possible strings
# we could create.
# 
# 
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
# 
# Input: S = "12345"
# Output: ["12345"]
# 
# 
# Note:
# 
# 
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
# 
# 
#
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.res = []
        self.length = len(S)

        self.dfs(S, '', 0)
        return self.res

    def dfs(self, s, sub_set, index):
        if index == self.length:
            return self.res.append(sub_set)    
                    
        if s[index].isalpha():
            self.dfs(s, sub_set + s[index].upper(), index+1)
            self.dfs(s, sub_set + s[index].lower(), index+1)
        else:
            self.dfs(s, sub_set + s[index], index+1)
