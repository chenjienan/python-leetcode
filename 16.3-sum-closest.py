#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (42.88%)
# Total Accepted:    312.6K
# Total Submissions: 729.1K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums) - 2):
            # establish counter 2 pointers
            lo, hi = i + 1, len(nums) - 1

            while lo < hi:
                s = nums[lo] + nums[hi] + nums[i]
                if s == target: return s
                
                if abs(target - s) < abs(target - res):
                    res = s
                
                if s < target:  lo += 1
                else: hi -= 1

        return res

