#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # reorganize the array from the end of the array
        last = m + n - 1    # mark the last index

        while m > 0 and n > 0:
            # take the larger one
            # and put it to the end of the array
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        if n > m:
            nums1[:n] = nums2[:n]
