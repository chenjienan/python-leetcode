#
# @lc app=leetcode id=89 lang=python
#
# [89] Gray Code
#
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # two successive values differ in only one bit.
        # reduce switching operations
        if n == 0: return [0]
        
        res = self.grayCode(n - 1)
        seq = list(res)
        for i in reversed(res):
            seq.append((1 << (n - 1)) | i)
            
        return seq

