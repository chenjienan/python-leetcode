#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits):
        s = ''
        for d in digits:
            s += str(d)

        plus_one = int(s) + 1

        return [int(d) for d in str(plus_one)]

s = Solution()
s.plusOne([1,2,3])