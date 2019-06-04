#
# @lc app=leetcode id=179 lang=python
#
# [179] Largest Number
#
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        s_nums = map(str, nums)
        res = ''.join(sorted(s_nums, key = LargerNumKey))
        return '0' if res[0] == '0' else res
        

