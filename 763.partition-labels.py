#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (69.29%)
# Total Accepted:    40.9K
# Total Submissions: 59K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 
# A string S of lowercase letters is given.  We want to partition this string
# into as many parts as possible so that each letter appears in at most one
# part, and return a list of integers representing the size of these parts.
# 
# 
# Example 1:
# 
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
# 
# 
# 
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
# 
#
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        d = {}
        res = []
        
        # store last index of each char
        for i, v in enumerate(S):
            d[v] = i

        # 2 pointers same direction
        start, end = 0, 0
        for j, v in enumerate(S):
            end = max(end, d[v])     # check the last index of cur char
            if j == end:                # self-contained
                res.append(end - start + 1)
                start = end + 1         # new starts
        return res
