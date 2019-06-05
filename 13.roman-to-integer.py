#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        _dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        number = 0

        for i in range(len(s) - 1):
            if _dict[s[i]] < _dict[s[i+1]]: # 前后比较
                number -= _dict[s[i]]       # 倒退
            else:
                number += _dict[s[i]]       # 前进
                
        return number + _dict[s[-1]]        # last letter is always added
