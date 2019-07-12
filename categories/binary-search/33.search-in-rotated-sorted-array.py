#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        n = len(nums)
        s, e = 0, n - 1

        # we can gurantee target is in the 
        # range (s, e)
        while s + 1 < e:
            m = s + (e - s) // 2

            if nums[m] == target: return m
            # 以 m 为参照, 探索地形
            elif nums[s] < nums[m]:     #地形1
                if nums[s] <= target <= nums[m]: e = m
                else: s = m
            else:                       #地形2
                if nums[m] <= target <= nums[e]: s = m
                else: e = m
            
        if nums[s] == target: return s
        if nums[e] == target: return e
        return -1
