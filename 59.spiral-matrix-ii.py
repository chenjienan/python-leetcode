#
# @lc app=leetcode id=59 lang=python
#
# [59] Spiral Matrix II
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        res = [[0 for _ in range(n)] for _ in range(n)]

        left = 0
        right = n-1
        top = 0
        bottom = n-1

        num = 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                res[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left-1, -1):
                res[bottom][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom, top-1, -1):
                res[i][left] = num
                num += 1
            left += 1
        
        return res
