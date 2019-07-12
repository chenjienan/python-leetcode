#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
from collections import deque

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0

        rows = len(grid)
        cols = len(grid[0])

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, self.bfs(grid, r, c))

        return res
    
    def bfs(self, grid, x, y):
        local_max = 1
        grid[x][y] = 0  # set to sea
        queue = deque([(x, y)])
        while queue:
            cur_x, cur_y = queue.popleft() 
            for d_x, d_y in DIRECTIONS:
                nxt_x = cur_x + d_x
                nxt_y = cur_y + d_y

                if 0 <= nxt_x < len(grid) and \
                   0 <= nxt_y < len(grid[0]) and \
                   grid[nxt_x][nxt_y] == 1:
                   
                   grid[nxt_x][nxt_y] = 0
                   queue.append((nxt_x, nxt_y))
                   local_max += 1
        
        return local_max
