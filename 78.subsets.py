#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res, 0)
        
        return res
        
    def dfs(self, nums, subset, res, i):
        if i == len(nums):
            if subset in res: 
                return
            else:
                res.append(subset)
                return
            
        self.dfs(nums, subset + [nums[i]], res, i + 1)   # add next
        self.dfs(nums, subset, res, i + 1)   # add itself

