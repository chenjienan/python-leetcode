#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ls = [x for x in range(1, 10)]

        # unique set of numbers
        res = []
        self.helper(ls, n, k, [], 0, res)

        return res
    
    def helper(self, c, remain, length, cur_subset, cur_index, res):
        if remain == 0 and cur_subset not in res and len(cur_subset) == length:
            return res.append(cur_subset)
        
        for i in range(cur_index, len(c)):
            if c[i] > remain: return 
            
            self.helper(c[:i] + c[i+1:], remain - c[i], length, cur_subset + [c[i]], i, res)

