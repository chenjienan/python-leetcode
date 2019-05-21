#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#
NEI_LOCATIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):

                lives = self.live_neighbors(board, r, c, rows, cols)
                # 如果当前位置为活细胞，且相邻活细胞数量为2个或者3个，则下一状态仍为活细胞
                if board[r][c] == 1 and lives >= 2 and lives <= 3:  
                    board[r][c] = 3
                
                # 如果当前位置为死细胞，且相邻活细胞数量为3个，则下一状态为活细胞
                if board[r][c] == 0 and lives == 3:
                    board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                board[r][c] >>= 1

    def live_neighbors(self, board, r, c, rows, cols):
        lives = 0

        for d_x, d_y in NEI_LOCATIONS:
            nei_x, nei_y = r + d_x, c + d_y

            if 0 <= nei_x < rows and \
                0 <= nei_y < cols:
                lives += board[nei_x][nei_y] & 1

        return lives
    # def live_neighbors(self, board, i, j, m, n):
    #     lives = 0
    #     for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
    #         for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
    #             lives += board[x][y] & 1
    #     lives -= board[i][j] & 1
    #     return lives