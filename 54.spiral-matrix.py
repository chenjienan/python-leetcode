#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        res = []
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        direction = 0

        while True:

            if direction == 0: # from left to right
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            
            elif direction == 1: # from top to bottom
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            
            elif direction == 2: # from right to left
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            
            else:   # from bottom to top
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1

            # exit the loop:
            if up > down or left > right: return res
            direction = (direction + 1) % 4

