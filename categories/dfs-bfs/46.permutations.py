#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (53.66%)
# Total Accepted:    349.4K
# Total Submissions: 649K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        length = len(nums)                                              
        self.dfs(nums, [], length, res)
        return res
    
    def dfs(self, choices, subset, length, res):
        if len(subset) == length:
            res.append(subset)
        
        for i in range(len(choices)):
            self.dfs(choices[:i] + choices[i+1:], subset + [choices[i]], length, res)
    #     res = []
    #     self.dfs(nums, [], res, len(nums))
    #     return res

    # def dfs(self, nums, sub_set, res, l):
    #     if len(sub_set) == l: 
    #         return res.append(sub_set)

    #     for i in range(len(nums)):
    #         self.dfs(nums[:i] + nums[i+1:], sub_set + [nums[i]], res, l)            


