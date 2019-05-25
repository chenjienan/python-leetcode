#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals: return []
        # sorted by start time
        intervals = sorted(intervals, key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            last = res[-1]
            if last[1] >= intervals[i][0]:
                last[1] = max(intervals[i][1], last[1])
            else:
                res.append(intervals[i])
        
        return res
