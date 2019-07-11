#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        
        n = len(nums)
        # compare from the right side
        first_small = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                # found the first small
                first_small = i
                break
        # cannot find the first small
        # the list is descending
        if first_small == -1: 
            nums.sort()
            return

        first_large = -1
        for j in range(n-1, i, -1):
            if nums[j] > nums[first_small]:
                # found the first number larger than first small
                first_large = j
                break
        
        nums[first_small], nums[first_large] = nums[first_large], nums[first_small]
        # reverse the section [i+1:]
        nums[first_small+1:] = sorted(nums[first_small+1:])
        
        

