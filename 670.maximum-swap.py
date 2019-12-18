#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int):
        ls_num = list(int(x) for x in str(num))
        reversed_ls_num = sorted(ls_num, reverse=True)
        
        # get the first diff (reversed_ls_sum is always > than the one in ls_num)
        i = 0
        while i < len(ls_num) and ls_num[i] == reversed_ls_num[i]:
            i += 1
        
        # corner case: original int is max
        if i == len(ls_num):
            return self.convertListToInt(ls_num)
            
        pos_small = i
        pos_large = 0
        
        # get the last index of the smaller value
        for i, v in enumerate(ls_num):
            if v == reversed_ls_num[pos_small]:
                pos_large = i

        ls_num[pos_small], ls_num[pos_large] = ls_num[pos_large], ls_num[pos_small]
        
        return self.convertListToInt(ls_num)
    
    def convertListToInt(self, ls):
        res = 0
        for i, v in enumerate(ls[::-1]):
            res += v * 10 ** i
        
        return res
# @lc code=end

