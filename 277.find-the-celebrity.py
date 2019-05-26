#
# @lc app=leetcode id=277 lang=python
#
# [277] Find the Celebrity
#
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 默认第一位是0
        # 过一遍
        candidate = 0
        for i in range(1, n):
            # 如果认识一位,就不是名人
            if knows(candidate, i): candidate = i
            
        # 检验:名人不认识任何人
        for i in range(n):
            # knows(A, B) A knows B
            if candidate != i and knows(candidate, i): return -1
        
        # 检验: 每个人都认识名人
        for i in range(n):
            if candidate != i and not knows(i, candidate): return -1
        
        return candidate
