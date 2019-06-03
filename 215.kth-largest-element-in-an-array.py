#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#
import heapq
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pivot_i = random.randint(left, right)
            new_pivot_i = self.partition(nums, left, right, pivot_i)

            if new_pivot_i == k -1:     # index
                return nums[new_pivot_i]
            elif new_pivot_i > k - 1:   # go left
                right = new_pivot_i - 1
            else:                       # go right
                left = new_pivot_i + 1
        return -1
    
    def partition(self, nums, left, right, pivot_i):
        pivot_val = nums[pivot_i]
        
        # move pivot to end
        nums[pivot_i], nums[right] = nums[right], nums[pivot_i]
        # move all smaller elements to the left
        new_pivot_i = left
        for i in range(left, right):
            if nums[i] < pivot_val:
                nums[new_pivot_i], nums[i] = nums[i], nums[new_pivot_i]
                new_pivot_i += 1
        # move pivot to its findal place
        nums[right], nums[new_pivot_i] = nums[new_pivot_i], nums[right]
        
        return new_pivot_i


s = Solution()
s.findKthLargest([3, 2, 1, 5, 6, 4], 2)