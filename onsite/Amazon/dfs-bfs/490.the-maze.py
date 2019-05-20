#
# @lc app=leetcode id=490 lang=python
#
# [490] The Maze
#
import collections
DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze: return False
        # 基本包
        rows = len(maze)
        cols = len(maze[0])
        return self._dfs(maze, start[0], start[1], rows, cols, destination)
        # queue = collections.deque([start])
        
        # while queue:
        #     x, y = queue.popleft()
        #     # mark visited
        #     maze[x][y] = '#'
        #     # check if arrived
        #     if x == destination[0] and y == destination[1]: return True
        #     for d_x, d_y in DIRECTION:
        #         nxt_x, nxt_y = x, y
        #         # 每次选一个方向滚到底
        #         while 0 <= nxt_x < rows and 0 <= nxt_y < cols and \
        #             maze[nxt_x][nxt_y] != 1:
        #             nxt_x += d_x
        #             nxt_y += d_y

        #         # x and y locates @ a wall when exiting the above while loop, so we need to backtrack 1 position
        #         nxt_x -= d_x
        #         nxt_y -= d_y

        #         # Check if the new starting position has been visited
        #         if maze[nxt_x][nxt_y] == 0: queue.append([nxt_x, nxt_y])
        
        # return False

    def _dfs(self, maze, x, y, rows, cols, dest):
        # base case
        if maze[x][y] == '#': return False
        if [x, y] == dest: return True

        maze[x][y] = '#'
        for d_x, d_y in DIRECTION:
            nxt_x, nxt_y = x, y
            # 每次选一个方向滚到底
            while 0 <= nxt_x < rows and 0 <= nxt_y < cols and \
                maze[nxt_x][nxt_y] != 1:
                nxt_x += d_x
                nxt_y += d_y
            nxt_x -= d_x
            nxt_y -= d_y

            if self._dfs(maze, nxt_x, nxt_y, rows, cols, dest): return True
        return False