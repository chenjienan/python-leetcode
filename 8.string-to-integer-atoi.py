#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # if not s: return 0
        ls = list(s.strip())
        if not ls: return 0
        sign = 1
        if ls[0] in ['-', '+']:
            if ls[0] == '-':
                sign = -1 
            ls = ls[1:]
                    
        
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            res = res*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * res, 2**31-1))

