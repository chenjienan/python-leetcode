#
# @lc app=leetcode id=733 lang=python
#
# [733] Flood Fill
#

DIRECTION = [[-1, 0], [1, 0], [0, 1], [0, -1]]
import collections

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        # 与number of island相似
        # 不同点在于起始点已经提供,直接进queue处理一轮即可
        oldColor = image[sr][sc]
        # check if oldColor is already painted
        if oldColor != newColor:
            self.bfs(image, sr, sc, oldColor, newColor)

        return image

    def bfs(self, image, r, c, old, new):
        image[r][c] = new

        rows = len(image)
        cols = len(image[0])
        queue = collections.deque([(r, c)])

        while queue:
            x, y = queue.popleft()

            for d_x, d_y in DIRECTION:
                new_x, new_y = x + d_x, y + d_y

                # boundary check
                if 0 <= new_x < rows and \
                    0 <= new_y < cols and \
                    image[new_x][new_y] == old:
                    # change color
                    image[new_x][new_y] = new
                    queue.append((new_x, new_y))
