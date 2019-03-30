#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.22%)
# Total Accepted:    7.6K
# Total Submissions: 16.4K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
#

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = []
        count, res = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: count += 1
                if grid[r][c] == 2: queue.append((r, c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                for _x, _y in DIRECTIONS:
                    nxt_r = r + _x
                    nxt_c = c + _y

                    if 0 <= nxt_r < rows and \
                        0 <= nxt_c < cols and \
                        grid[nxt_r][nxt_c] == 1:
                        grid[nxt_r][nxt_c] = 2
                        count -= 1
                        queue.append((nxt_r, nxt_c))
            res += 1
        return max(0, res-1) if count == 0 else -1 

