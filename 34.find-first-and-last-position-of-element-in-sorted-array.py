#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        
        t_index = -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                t_index = mid
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if t_index == -1:
            return [-1, -1]
        # print(t_index)
        min_i, max_i = 0, len(nums) - 1

        i = t_index
        while i > 0:
            if nums[i-1] != nums[i]:
                min_i = i
                break
            i -= 1
        
        j = t_index
        while j < len(nums) - 1:
            if nums[j+1] != nums[j]:
                max_i = j
                break
            j += 1


        return [min_i, max_i]



s = Solution()
# print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([5,7,7,8,8,10], 8))

# 4pm
# binary searh
# find the target index

        

