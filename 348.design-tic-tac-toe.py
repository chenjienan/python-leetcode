#
# @lc app=leetcode id=348 lang=python
#
# [348] Design Tic-Tac-Toe
#
class TicTacToe(object):

    def __init__(self, n):
        self.n = n      # total number
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row, col, player):
        '''
        assign the value of 1 for player 1 and -1 for player 2
        '''
        player_val = 1 if player == 1 else -1
        self.row[row] += player_val
        self.col[col] += player_val

        if row == col:
            self.diag += player_val
            if abs(self.diag) == self.n: return player      # win case 1
        
        if (self.n -1 - row) == col:
            self.anti_diag += player_val
            if abs(self.anti_diag) == self.n: return player # win case 2
        
        if abs(self.row[row]) == self.n or \
           abs(self.col[col]) == self.n: return player      # win case3, 4
        
        return 0


