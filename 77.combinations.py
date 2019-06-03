#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # enumerate a list from 1 to n
        nums = list(range(1, n+1))
        res = []
        self.dfs(nums, k, [], 0, res)
        return res
    
    def dfs(self, nums, k, subset, index, res):
        if len(subset) == k:
            res.append(subset)
            return
        
        for i in range(index, len(nums)):
            # i + 1: move to next
            # i: add self
            self.dfs(nums, k, subset + [nums[i]], i+1, res)

