#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (38.82%)
# Total Accepted:    175.3K
# Total Submissions: 451.5K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#


# DP
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)       # height of the triangle

        f = [[float('inf') for _ in range(n)] for _ in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    val = f[i-1][j]
                else:
                    val = min(f[i-1][j], f[i-1][j-1])
                
                f[i][j] = triangle[i][j] + val
        
        return min(f[-1])


