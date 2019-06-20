#
# @lc app=leetcode id=245 lang=python3
#
# [245] Shortest Word Distance III
#
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx_1, idx_2, min_dist = float('inf'), float('inf'), len(words)
        
        if word1 == word2:
            for i, v in enumerate(words):
                if v == word1:
                    min_dist = min(min_dist, abs(i - idx_1))
                    idx_1 = i
        else:
            for i, v in enumerate(words):
                if v == word1:
                    idx_1 = i
                elif v == word2:
                    idx_2 = i
                
                min_dist = min(min_dist, abs(idx_1 - idx_2))
                
        return min_dist

