#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

MAPPING = {
            "0": " ",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []

        res = []
        self.dfs(digits, 0, '', res)
        return res

    def dfs(self, digits, index, s, res):
        '''
        index keeps tracking the current position
        s is the substring
        recursively add qualified substring to res
        '''

        if index == len(digits): return res.append(s)        
        for ch in MAPPING[digits[index]]:
            self.dfs(digits, index + 1, s + ch, res)


