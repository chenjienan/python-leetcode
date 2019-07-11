#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        self.helper(candidates, target, [], 0, res)
        return res

    # 元素不可重复
    def helper(self, c, remain, cur_subset, index, res):
        if remain == 0 and cur_subset not in res:
            return res.append(cur_subset)
        
        for i in range(index, len(c)):
            if c[i] > remain: return       
            self.helper(c[:i] + c[i+1:], remain - c[i], cur_subset + [c[i]], i, res)

s = Solution()
s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)