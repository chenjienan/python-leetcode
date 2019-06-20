#
# @lc app=leetcode id=244 lang=python3
#
# [244] Shortest Word Distance II
#

import collections

class WordDistance:

    def __init__(self, words):
        self.d = collections.defaultdict(list)
        for i, v in enumerate(words):
            self.d[v].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        ls_1 = self.d[word1]
        ls_2 = self.d[word2]

        min_dist = float('inf')
        for idx_1 in ls_1:
            for idx_2 in ls_2:
                min_dist = min(min_dist, abs(idx_1 - idx_2))
        
        return min_dist


# hash-table: 
a: [0, 5]
b: [1]
c: [2]
# Your WordDistance object will be instantiated and called as such:
words = ['a', 'b', 'a', 'c']
obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

