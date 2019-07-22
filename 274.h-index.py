#
# @lc app=leetcode id=274 lang=python
#
# [274] H-Index
#
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        
        for i, v in enumerate(citations):
            if v >= n - i: return n-i
            
        return 0

#             idx 0 1 2 3 4 
#           n-idx 5 4 3 2 1  => h
#   citation[idx] 0 1 3 5 6