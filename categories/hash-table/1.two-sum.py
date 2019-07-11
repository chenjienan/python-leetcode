#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # key: num value: index
        h = {}
        for i in range(len(nums)):
            h[target - nums[i]] = i

        # x + y = target
        for i, num in enumerate(nums):
            if num in h and i != h[num]: return i, h[num]
        
        return -1

