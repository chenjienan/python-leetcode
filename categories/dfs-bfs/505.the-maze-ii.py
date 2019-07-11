#
# @lc app=leetcode id=505 lang=python
#
# [505] The Maze II
#
import heapq
DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze: return False
        # 基本包
        rows = len(maze)
        cols = len(maze[0])

        # min heap: the distance value has to be the first element
        heap = [(0, start[0], start[1])]
        visited = set()
        
        while heap:
            dist, x, y = heapq.heappop(heap)
            # check if visited
            if (x, y) in visited: continue
            visited.add((x, y))
            # check if arrived
            if x == destination[0] and y == destination[1]: return dist
            for d_x, d_y in DIRECTION:
                nxt_x, nxt_y = x + d_x, y + d_y
                cur_dist = dist
                # 每次选一个方向滚到底
                while 0 <= nxt_x < rows and 0 <= nxt_y < cols and \
                    maze[nxt_x][nxt_y] == 0:
                    nxt_x += d_x
                    nxt_y += d_y
                    cur_dist += 1

                # x and y locates @ a wall when exiting the above while loop, so we need to backtrack 1 position
                nxt_x -= d_x
                nxt_y -= d_y

                # Check if the new starting position has been visited
                if maze[nxt_x][nxt_y] not in visited: 
                    heapq.heappush(heap, (cur_dist, nxt_x, nxt_y))
        
        return -1

