#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (39.35%)
# Total Accepted:    226.6K
# Total Submissions: 574K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []        
        if not nums: return self.res        
        self.length = len(nums)
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, sub_set):
        if len(sub_set) == self.length and \
            sub_set not in self.res: 
            return self.res.append(sub_set)

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], sub_set + [nums[i]])      

