#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#
import collections

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]

class Solution:
    def updateBoard(self, board, click):
        
        self.rows = len(board)
        self.cols = len(board[0])

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        # 记录已经走过的点
        visited = set()

        queue = collections.deque([click])
        visited.add((click[0], click[1]))

        while queue:
            r, c = queue.popleft()

            cnt = 0
            for d_x, d_y in DIRECTIONS:
                nxt_x = r + d_x
                nxt_y = c + d_y

                if 0 <= nxt_x < self.rows and \
                0 <= nxt_y < self.cols and \
                board[nxt_x][nxt_y] == 'M':
                    cnt += 1

            board[r][c] = str(cnt) if cnt else 'B'


            for d_x, d_y in DIRECTIONS:
                nxt_x = r + d_x
                nxt_y = c + d_y

                if 0 <= nxt_x < self.rows and \
                   0 <= nxt_y < self.cols and \
                   (nxt_x, nxt_y) not in visited and \
                   board[r][c] == 'B' and \
                   board[nxt_x][nxt_y] == 'E':
                   queue.append((nxt_x, nxt_y))
                   visited.add((nxt_x, nxt_y))
        
        return board
