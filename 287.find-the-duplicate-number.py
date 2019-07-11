#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            m = l + (r - l) // 2 
            cnt = sum(num <= m for num in nums)
            
            if cnt > m:
                r = m - 1
            else:                
                l = m + 1
        
        return l

