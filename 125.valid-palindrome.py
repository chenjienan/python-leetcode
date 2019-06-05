#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()

        left, right = 0, len(new_str) - 1

        while left < right:
            if new_str[left] != new_str[right]:
                return False
            
            left += 1
            right -= 1
        
        return True

