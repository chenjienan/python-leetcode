#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            
            if ch in ')]}':
                if not stack: return False
                
                last_p = stack.pop()
                if (ch == ')' and last_p != '(') or \
                    (ch == ']' and last_p != '[') or \
                    (ch == '}' and last_p != '{'):
                   return False
                
        return False if stack else True  

