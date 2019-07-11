#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        self.helper(candidates, target, [], 0, res)

        return res

    def helper(self, c, remain, cur_subset, index, res):
        if remain == 0:
            return res.append(cur_subset)
        
        for i in range(index, len(c)):
            if c[i] > remain: return         
            self.helper(c, remain - c[i], cur_subset + [c[i]], i, res)





