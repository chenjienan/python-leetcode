#
# @lc app=leetcode id=448 lang=python
#
# [448] Find All Numbers Disappeared in an Array
#
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # numbers are 1 to n 
        # so that we have to minus 1
        for d in nums:
            index = abs(d) - 1
            nums[index] = -abs(nums[index])     # turn the index into negative
                    
        # if the value of the index is positive => missing
        res = [i + 1 for i in range(len(nums)) if nums[i] > 0]
        return res

