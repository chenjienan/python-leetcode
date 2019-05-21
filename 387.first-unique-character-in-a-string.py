#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        
        for i, v in enumerate(s):
            if counter[v] == 1:
                return i
        
        return -1

