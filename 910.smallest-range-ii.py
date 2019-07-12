#
# @lc app=leetcode id=910 lang=python3
#
# [910] Smallest Range II
#
class Solution:
    def smallestRangeII(self, A: List[int], K: int):
        A.sort()
        max_val = A[len(A) - 1]
        min_val = A[0]
        min_range = max_val - min_val
        
        for i in range(len(A) - 1):
            min_range = min(min_range, max(max_val - K, A[i] + K) - min(min_val + K, A[i+1] - K))
            
        return min_range

