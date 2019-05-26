#
# @lc app=leetcode id=280 lang=python
#
# [280] Wiggle Sort
#
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # One pass O(n)
        n = len(nums)
        should_swap = True
        # 理顺逻辑, 保证本Index和 next index之间的关系
        # 边界条件需要注意从0开始, n-1结束, 因为有n+1
        for i in range(0, n-1):
            if should_swap:
                # 再加条件: 需要检查cur index和next index
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

            # 不许交换也要保证本index < next index
            else:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            
            should_swap = not should_swap

        # O(nlogn)
        # 1. sort
        # 2. swap for odd index 
        # 排序, 错开index作交换
        # nums.sort()
        # n = len(nums)
        # for i in range(n-1):
        #     if i % 2 != 0:
        #         nums[i], nums[i+1] = nums[i+1], nums[i]
            
