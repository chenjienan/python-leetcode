#
# @lc app=leetcode id=140 lang=python
#
# [140] Word Break II
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # DFS + memo
        wordDict = set(wordDict)
        return self.canBreak(s, wordDict, {})
    
    
    # memo stores all possible answers for [0:index] 
    # and memo is a dictionary
    def canBreak(self, s, wordDict, memo):
        if s in memo: return memo[s]
        
        res = []
        if s in wordDict: res.append(s)            

        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            if right in wordDict:
                # add right section to all possiable answers
                res += [w + " " + right for w in self.canBreak(left, wordDict, memo)]                

        memo[s] = res
        return memo[s]

