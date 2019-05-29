#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # base case
        if not a: return b
        if not b: return a
        
        # inductive case
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'


# The time complex is O(m+n+c)，it's linear, 
# where m=len(a)，n=len(b) and c="count of carries, 
# which is less than min(m,n)".


