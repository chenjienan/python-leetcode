#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start: track the position of the longest substring
        res, start = 0, -1
        # key: char
        # value: the right-most index
        d = {}

        for end, v in enumerate(s):
            # if we found a repeated char
            # update the start position
            if v in d and start < d[v]:
                start = d[v]
            # else, update the res
            else:
                res = max(res, end - start) # end - start is the cur length

            # update the dict according to current position
            d[v] = end
        return res
