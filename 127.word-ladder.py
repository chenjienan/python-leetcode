#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#

import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        res = 0
        if endWord not in wordList: return res
        wordList = set(wordList)
        # (word, distance)
        queue = collections.deque([(beginWord, 1)])
        visited = set(beginWord)

        while queue:
            word, dist = queue.popleft()
            if word == endWord: return dist

            for new_word in self.new_words_with_one_dist(word):
                if new_word not in visited and new_word in wordList:
                    queue.append((new_word, dist+1))
                    visited.add(new_word)
        return 0
    
    # create new word within distance 1
    def new_words_with_one_dist(self, word):
        new_word_ls = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c != word[i]:
                    new_word_ls.append(word[:i] + c + word[i+1:])
        
        return new_word_ls
                    
        
        
#


