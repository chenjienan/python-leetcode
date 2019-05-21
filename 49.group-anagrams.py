#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (45.06%)
# Total Accepted:    302.7K
# Total Submissions: 671.8K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#
class Solution:
    def groupAnagrams(self, strs):
        # key: sorted str
        # value: list of anagram
        d = {}
        for w in strs:
            key = ''.join(sorted(w))
            if key in d:
                d[key].append(w)
            else:
                d[key] = [w]        
            
        return [v for v in d.values()]

# eat => aet

