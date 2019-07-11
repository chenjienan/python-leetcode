#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # clockwise rotate
        # first reverse **up to down, then swap the symmetry 
        # 1 2 3     7 8 9     7 4 1
        # 4 5 6  => 4 5 6  => 8 5 2
        # 7 8 9     1 2 3     9 6 3

        rows = len(matrix)
        cols = len(matrix[0])

        matrix.reverse()
        # traverse the upper triangle only
        for r in range(rows):
            for c in range(r + 1, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        
