#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        # 同向双指针
        # left 为当前能盈利的值
        left = prices[0]
        max_profit = 0

        # p 右指针
        for p in prices[1:]:
            cur_profit = p - left
            
            if cur_profit > 0:
                max_profit += cur_profit
            
            left = p
        
        return max_profit

