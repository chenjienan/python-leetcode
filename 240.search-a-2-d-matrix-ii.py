#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False

        rows = len(matrix)
        cols = len(matrix[0])

        # bottom - left
        r = rows - 1
        c = 0
        while r >= 0 and c <= cols - 1:
            cur = matrix[r][c]
 
            if cur == target: return True
            elif cur > target:
                r -= 1
            
            else:
                c += 1
            
        return False

s = Solution()
s.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]], 20)

# start from bottom - left corner
# cur > target => r - 1
# cur < target => c + 1