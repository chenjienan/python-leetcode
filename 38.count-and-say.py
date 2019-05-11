#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(1, n):
            s = self.read(s)
        return s
    
    def read(self, s):
        count = 0
        cur_str = ""

        for i in range(len(s)):
            if i == 0 or s[i] == s[i-1]:
                count += 1
            else:
                cur_str += str(count) + s[i-1] 
                count = 1
        
        cur_str += str(count) + s[len(s)-1]
        return cur_str

