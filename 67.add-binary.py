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
        carry = 0
        
        res = ""
        while a and b:
            num, carry = self.add(a[-1], b[-1], carry)
            res += num
            a = a[:-1]
            b = b[:-1]
        
        while a: 
            num, carry = self.add(a[-1], '0', carry)
            res += num
            a = a[:-1]
        while b: 
            num, carry = self.add(b[-1], '0', carry)
            res += num
            b = b[:-1]
            
        if carry: res += '1'
        
        return res[::-1]
                
    def add(self, a, b, carry):
        if a[-1] == '1' and b[-1] == '1':
            if carry: return '1', 1
            else: return '0', 1
        
        elif (a[-1] == '1' and b[-1] == '0') or \
             (a[-1] == '0' and b[-1] == '1'):
            if carry: return '0', 1
            else: return '1', 0
        
        else:
            if carry: return '1', 0
            else: return '0', 0
                
        # # base case
        # if not a: return b
        # if not b: return a
        
        # # inductive case
        # if a[-1] == '1' and b[-1] == '1':
        #     return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        # if a[-1] == '0' and b[-1] == '0':
        #     return self.addBinary(a[0:-1],b[0:-1])+'0'
        # else:
        #     return self.addBinary(a[0:-1],b[0:-1])+'1'


# The time complex is O(m+n+c)，it's linear, 
# where m=len(a)，n=len(b) and c="count of carries, 
# which is less than min(m,n)".


