#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if not nums or n < 3: return []
        if n == 3 and sum(nums) == 0: return [nums]
        # output is a solution set, so that we
        # can sort the list
        nums.sort()
        # use hashset to improve performance
        res = set()
        for i in range(n - 2):
            # basically, it's performing 2 sum
            left = i + 1    # left bound
            right = n -1    # right bound
            target = -nums[i]
            while left < right:
                # a + b = -c
                if nums[left] + nums[right] == target:
                    ans = (nums[left], nums[right], -target)
                    res.add(ans)
                    # move to next
                    left += 1
                    right -= 1
                    # 去重
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
                elif nums[left] + nums[right] < target: 
                    # increment left
                    left += 1
                else:
                    right -= 1

        return list(res)

        

