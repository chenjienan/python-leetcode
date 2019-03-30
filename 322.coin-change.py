#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (29.55%)
# Total Accepted:    175.2K
# Total Submissions: 592.5K
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# Example 1:
# 
# 
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        f = [0] + [float('inf') for _ in range(amount)]
        
        for i in range(amount + 1):
            for c in coins:
                if i >= c:
                    f[i] = min(f[i], f[i - c] + 1)
        
        return f[amount] if f[amount] != float('inf') else -1

