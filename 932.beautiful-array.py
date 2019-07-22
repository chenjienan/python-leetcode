#
# @lc app=leetcode id=932 lang=python
#
# [932] Beautiful Array
#
class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        # key: n, value: possible permutated result
        memo = {1: [1]}
        return self.helper(N, memo)
        
    
    def helper(self, N, memo):
        if N not in memo:
            odds = self.helper((N+1) / 2, memo)
            evens = self.helper(N / 2, memo)
            memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
        return memo[N]
        

