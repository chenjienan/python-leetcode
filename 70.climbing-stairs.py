#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (43.72%)
# Total Accepted:    372.6K
# Total Submissions: 852.4K
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#
class Solution:
    def climbStairs(self, n: int) -> int:
        # # 有多少种解法 - 单序列问题
        
        # if n == 1: return 1
        
        # # 设置状态为x个阶梯,有f[x]种走法
        # f = [None for _ in range(n)]     # 1D 贮存
        # f[0] = 1                        # 初始化:走第一步有1种方法
        # f[1] = 2                        # 初始化:走第二步有2种方法

        # for i in range(2, n):
        #     f[i] = f[i-1] + f[i-2]      # 转移方程 dp[n] = dp[n-1]+dp[n-2]
        # return f[-1]                    # 返回结果为最后一个计算答案

        # 滚动数组解法
        # f[i] 只与f[i-1]和f[i-2]有关系
        if n == 1: return 1

        f = [None for _ in range(2)]
        f[0] = 1
        f[1] = 2

        for _ in range(2, n):
            new = f[0] + f[1]
            f[0], f[1] = f[1], new

        return f[1]
        
