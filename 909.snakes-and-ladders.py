#
# @lc app=leetcode id=909 lang=python
#
# [909] Snakes and Ladders
#

import collections
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        queue = collections.deque([(1, 0)])
        visited = {1}

        while queue:
            cur_num, dist = queue.popleft()

            if cur_num == N*N: return dist
            
            for next_num in range(cur_num + 1, min(cur_num+6, N*N) + 1):
                r, c = self.get_coordinates(next_num, N)
                # ladder or snake
                if board[r][c] != -1: 
                    next_num = board[r][c]
                if next_num not in visited:
                    queue.append((next_num, dist + 1))
                    visited.add(next_num)

        return -1                

    def get_coordinates(self, num, N):
        '''
        Given a number, return the board coordinates (r, c)
        the row changes every N squares, and so is only based on quot = (s2-1) / N
        the column is only based on rem = (s2-1) % N and what row we are on (forwards or backwards.)
        '''
        q, r = divmod(num - 1, N)
        row = N - 1 - q
            #forward                        #backward
        col = r if row % 2 != N % 2 else N - 1 - r
        return row, col

