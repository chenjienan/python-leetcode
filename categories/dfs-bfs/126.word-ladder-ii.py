#
# @lc app=leetcode id=126 lang=python
#
# [126] Word Ladder II
#

import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList: return []
        wordList = set(wordList)
        wordList.add(beginWord)
        wordList.add(endWord)
        # key: word, value: distance
        dist = {}

        # set the distance
        self.bfs(endWord, beginWord, dist, wordList)
        res =  []
        self.dfs(beginWord, endWord, dist, wordList, [beginWord], res)
        return res

    # purpose of this function is to get the distance hash
    def bfs(self, start, end, dist, wordList):
        dist[start] = 0
        queue = collections.deque([start])

        while queue:
            word = queue.popleft()
            for new_word in self.word_list_in_dict(word, wordList):
                if new_word not in dist:
                    # add distance to new words
                    dist[new_word] = dist[word] + 1
                    queue.append(new_word)

    
    def word_list_in_dict(self, word, wordList):
        new_word_ls = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if c != word[i] and new_word in wordList:                    
                    new_word_ls.append(new_word)
        
        return new_word_ls

    def dfs(self, start, end, dist, wordList, path, res):
        if start == end: return res.append(list(path))
        
        for word in self.word_list_in_dict(start, wordList):
            if dist[word] == dist[start] - 1:
                path.append(word)
                self.dfs(word, end, dist, wordList, path, res)
                # backtracking
                path.pop()
