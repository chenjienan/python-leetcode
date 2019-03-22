#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (40.38%)
# Total Accepted:    150K
# Total Submissions: 371.3K
# Testcase Example:  '6'
#
# Write a program to check whether a given number is an ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# 
# Example 1:
# 
# 
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# 
# Example 2:
# 
# 
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# 
# 
# Example 3:
# 
# 
# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.
# 
# 
# Note:
# 
# 
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# 
#
class Solution:
    def isUgly(self, num: int) -> bool:
        
        # if num <= 0: return False
        # if num == 1: return True
        
        # while num >= 2 and num % 2 == 0: num /= 2
        # while num >= 3 and num % 3 == 0: num /= 3
        # while num >= 5 and num % 5 == 0: num /= 5
        
        # return num == 1

        if num > 0:
            for i in 2,3,5:
                while num % i == 0:
                    num /= i
        
        return num == 1
