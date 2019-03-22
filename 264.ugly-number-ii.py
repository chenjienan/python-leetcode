#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (35.66%)
# Total Accepted:    98.5K
# Total Submissions: 275.7K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # ugly = [1]

        # i2 = i3 = i5 = 0

        # # each prime 2, 3, 5 have an index to the next number that
        # # can be multiplied with the prime to produce a new ugly number

        # while len(ugly) < n:
        #     while ugly[i2] * 2 <= ugly[-1]: 
        #         i2 += 1
        #     while ugly[i3] * 3 <= ugly[-1]: 
        #         i3 += 1
        #     while ugly[i5] * 5 <= ugly[-1]: 
        #         i5 += 1
            
        #     ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        # return ugly[-1]

        # using heap
        # keep the store stores a tuple (val, factor)
        # factor value: the last factor that the number was multiplied to

        import heapq
        h = [(1, 1)]
        for _ in range(n):
            val, factor = heapq.heappop(h)
            for p in 2, 3, 5:
                if factor <= p:
                    heapq.heappush(h, (val * p, p))
        
        return val

