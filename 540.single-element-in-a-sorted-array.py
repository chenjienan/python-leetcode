#
# @lc app=leetcode id=540 lang=python
#
# [540] Single Element in a Sorted Array
#
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 1
        while r < len(nums):
            if nums[l] != nums[r]:
                break


            l += 2
            r += 2

        if l - 1 < 0 or nums[l-1] != nums[l]:
            return nums[l]
        else:
            return nums[r]

