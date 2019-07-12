#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#
import collections

DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0

        rows = len(grid)
        cols = len(grid[0])

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self._bfs(r, c, rows, cols, grid)
                    res += 1
        
        return res

    def _bfs(self, r, c, rows, cols, grid):
        grid[r][c] = '#'
        queue = collections.deque([(r, c)])
        while queue:
            x, y = queue.popleft()

            for d_x, d_y in DIRECTION:
                nxt_x, nxt_y = x + d_x, y + d_y
                if 0 <= nxt_x < rows and \
                    0 <= nxt_y < cols and \
                    grid[nxt_x][nxt_y] == '1':
                    grid[nxt_x][nxt_y] = '#'
                    queue.append((nxt_x, nxt_y))



        
