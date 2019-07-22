#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#
class Solution:
    def smallestRangeI(self, A, K):
        if len(A) == 1: return 0
        
        A.sort()
        
        if A[0] + K >= A[len(A)-1] - K:
            return 0
        
        return A[len(A)-1] - A[0] - 2 * K

