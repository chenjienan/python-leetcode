#
# @lc app=leetcode id=186 lang=python
#
# [186] Reverse Words in a String II
#
class Solution(object):
    def reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: None Do not return anything, modify str in-place instead.
        """
        
        # 变相手写reverse string
        # reverse the whole thing
        self.reverse_str(s, 0, len(s)-1)
        
        word_start = 0
        # reverse each word back
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse_str(s, word_start, i-1)    # not to include i
                word_start = i + 1
        
        # reverse te last word
        self.reverse_str(s, word_start, len(s)-1)

    def reverse_str(self, s, start, end):

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

s = Solution()
s.reverseWords(['a','b','c','d'])