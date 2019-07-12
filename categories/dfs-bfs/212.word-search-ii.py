#
# @lc app=leetcode id=212 lang=python
#
# [212] Word Search II
#
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

    #     # This solution is LTE
    #     # dfs + memo search
    #     if not board or not board[0] or not words: return []
        
    #     rows = len(board)
    #     cols = len(board[0])

    #     # prevent LTE
    #     word_set = set(words)
    #     prefix_set = set()
    #     for word in words:
    #         for i in range(len(word)):
    #             prefix_set.add(word[:i + 1])

    #     res = set()
    #     for word in words:
    #         for r in range(rows):
    #             for c in range(cols):
    #                 # check if word exists
    #                 self._dfs(board, word, r, c, rows, cols, word_set, prefix_set, [], res)
        
    #     return list(res)

    # # length of the word will change when recursed
    # def _dfs(self, board, word, r, c, rows, cols, word_set, prefix_set, visited, res):
    #     if word not in prefix_set:
    #         return
        
    #     if word in word_set:
    #         res.add(word)

    #     # search criteria
    #     # boundary check + isVisisted + cannot be self
    #     if r < 0 or r >= rows or c < 0 or c >= cols or \
    #         word[0] != board[r][c] or (r, c) in visited:
    #         return
        
    #     # word match, proceed next step
    #     visited.append((r, c))
    #     self._dfs(board, word[1:], r - 1, c, rows, cols, word_set, prefix_set, visited, res)
    #     self._dfs(board, word[1:], r + 1, c, rows, cols, word_set, prefix_set, visited, res)
    #     self._dfs(board, word[1:], r, c + 1, rows, cols, word_set, prefix_set, visited, res)
    #     self._dfs(board, word[1:], r, c - 1, rows, cols, word_set, prefix_set, visited, res)
    #     visited.pop()   # reset visited       

        if not board or not board[0] or not words: return []

        res = []
        trie = Trie()
        root = trie.root

        # construct the trie
        for word in words:
            trie.insert(word)
        
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                self._dfs(board, root, r, c, rows, cols, "", res)

        return res

    def _dfs(self, board, node, r, c, rows, cols, path, res):
        if node.isWord: 
            res.append(path)
            node.isWord = False     # reset

        # boundary check
        if r < 0 or r >= rows or \
            c < 0 or c >= cols:
            return

        tmp = board[r][c]
        node = node.children.get(tmp)   # find cur node (char)
        if not node: return 
        
        board[r][c] = '#'
        self._dfs(board, node, r+1, c, rows, cols, path + tmp, res)
        self._dfs(board, node, r-1, c, rows, cols, path + tmp, res)
        self._dfs(board, node, r, c+1, rows, cols, path + tmp, res)
        self._dfs(board, node, r, c-1, rows, cols, path + tmp, res)
        board[r][c] = tmp # reset

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node: return False
        return node.isWord

class TrieNode():
    def __init__(self):
        # default value is a TrieNode
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False