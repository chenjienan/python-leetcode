#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Log Files
#
# https://leetcode.com/problems/reorder-log-files/description/
#
# algorithms
# Easy (59.63%)
# Total Accepted:    14.1K
# Total Submissions: 23.6K
# Testcase Example:  '["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]'
#
# You have an array of logs.  Each log is a space delimited string of words.
# 
# For each log, the first word in each log is an alphanumeric identifier.
# Then, either:
# 
# 
# Each word after the identifier will consist only of lowercase letters,
# or;
# Each word after the identifier will consist only of digits.
# 
# 
# We will call these two varieties of logs letter-logs and digit-logs.  It is
# guaranteed that each log has at least one word after its identifier.
# 
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier, with the
# identifier used in case of ties.  The digit-logs should be put in their
# original order.
# 
# Return the final order of the logs.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4
# 7"]
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the
# identifier.
# 
# 
#
class Solution:
    def reorderLogFiles(self, logs):
        d_ls, l_ls = [], [] 
        ls = []
        for log in logs:
            if log.split()[1].isdigit():
                # The digit-logs should be put in their original order
                d_ls.append(log)
            else:
                l_ls.append(log)
        
        # The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
        l_ls.sort(key=lambda x: x.split()[0])
        l_ls.sort(key=lambda x: x.split()[1:])

        # letter-logs come before any digit-log
        return l_ls + d_ls
# s = Solution()
# s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])
