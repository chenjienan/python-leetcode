#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        # dfs + memo search
        if not board or not board[0] or not word: return False
        
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                # check if word exists
                if self._dfs(board, word, r, c, rows, cols, []): 
                    return True
        
        return False

    # length of the word will change when recursed
    # return boolean
    def _dfs(self, board, word, r, c, rows, cols, visited):
        # the word is found
        if not word: return True
        
        # search criteria
        # boundary check + isVisisted + cannot be self
        if r < 0 or r >= rows or c < 0 or c >= cols or \
            word[0] != board[r][c] or (r, c) in visited:
            return False
        
        # word match, proceed next step
        visited.append((r, c))
        nxt = self._dfs(board, word[1:], r - 1, c, rows, cols, visited) or \
                self._dfs(board, word[1:], r + 1, c, rows, cols, visited) or \
                self._dfs(board, word[1:], r, c + 1, rows, cols, visited) or \
                self._dfs(board, word[1:], r, c - 1, rows, cols, visited)
        if not nxt: visited.pop()   # reset visited
        return nxt        
