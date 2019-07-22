#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s = set()
        
        for r in range(9):
            for c in range(9):
                val = B[r][c]
                if val == '.': continue
                
                if (r, val) in s or (val, c) in s or (r//3, c//3, val) in s:
                    return False
                
                s.add((r, val))
                s.add((val, c))
                s.add((r//3, c//3, val))
        return True

