#
# @lc app=leetcode id=243 lang=python3
#
# [243] Shortest Word Distance
#
class Solution:
    def shortestDistance(self, words, word1, word2):
        idx_1, idx_2 = float('inf'), float('inf')
        min_dist = len(words)

        for i, v in enumerate(words):
            if v == word1:
                idx_1 = i
            elif v == word2:
                idx_2 = i

            min_dist = min(min_dist, abs(idx_1 - idx_2))
        
        return min_dist

s = Solution()
s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding')
