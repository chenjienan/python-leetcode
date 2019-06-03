#
# @lc app=leetcode id=442 lang=python
#
# [442] Find All Duplicates in an Array
#
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for d in nums:
            index = abs(d) - 1
            if nums[index] < 0:
                res.append(abs(d))
            nums[index] *= -1
        
        return res


