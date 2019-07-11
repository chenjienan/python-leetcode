#
# @lc app=leetcode id=694 lang=python
#
# [694] Number of Distinct Islands
#

DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS + hashset
        if not grid or not grid[0]: return 0
        
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        shapes = set()

        # if rows == 1 and cols == 1: return 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cur_shape = self._bfs(grid, r, c, rows, cols, shapes)
                    if cur_shape not in shapes:
                        res += 1
                        shapes.add(cur_shape)

        return res
    

    # return a shape for each island in the hashset
    def _bfs(self, grid, r, c, rows, cols, shapes):
        queue = collections.deque([(r, c)])
        shape = ''
        while queue:
            x, y = queue.popleft()

            for d_x, d_y in DIRECTION:
                nxt_x, nxt_y = x + d_x, y + d_y

                if 0 <= nxt_x < rows and \
                    0 <= nxt_y < cols and \
                    grid[nxt_x][nxt_y] == 1:
                    grid[nxt_x][nxt_y] = 0
                    queue.append((nxt_x, nxt_y))
                    # mark down the path
                    # 选择起始点做参照
                    path = str(nxt_x - r) + str(nxt_y - c)
                    shape += path
        return shape


