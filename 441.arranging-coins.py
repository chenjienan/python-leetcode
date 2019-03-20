#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (37.55%)
# Total Accepted:    64.7K
# Total Submissions: 172.3K
# Testcase Example:  '5'
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# ⁠
# Given n, find the total number of full staircase rows that can be formed.
# 
# n is a non-negative integer and fits within the range of a 32-bit signed
# integer.
# 
# Example 1:
# 
# n = 5
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# 
# Because the 3rd row is incomplete, we return 2.
# 
# 
# 
# Example 2:
# 
# n = 8
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# 
# Because the 4th row is incomplete, we return 3.
# 
# 
#
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # low, high, res = 1, n, 0

        # while low < high:
        #     mid = low + (high - low) // 2 
        #     if mid * (mid + 1) <= 2 * n:
        #         res = mid
        #         low = mid
        #     else:
        #         high = mid
        
        # return res

        start, end = 1, n
        while start <= end:
            mid = start + (end - start) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                start = mid + 1
            else:
                end = mid - 1

        return end

