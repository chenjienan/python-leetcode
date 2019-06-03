#
# @lc app=leetcode id=81 lang=python
#
# [81] Search in Rotated Sorted Array II
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        lo, hi = 0, len(nums)-1
        while lo + 1 < hi:
            mid = lo + (hi-lo)//2
            if nums[mid] < nums[hi]:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid
                else:
                    hi = mid - 1
            elif nums[mid] > nums[hi]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid 
                else:
                    lo = mid + 1
            else:
                hi -= 1
        
        if nums[lo] == target: return True
        if nums[hi] == target: return True
            
        return False
