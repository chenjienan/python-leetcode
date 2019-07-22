#
# @lc app=leetcode id=334 lang=python
#
# [334] Increasing Triplet Subsequence
#
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i_val = float('inf')
        j_val = float('inf')

        for cur in nums:
            if cur <= i_val:
                i_val = cur
            elif cur <= j_val:
                j_val = cur
            else:
                return True

        return False

