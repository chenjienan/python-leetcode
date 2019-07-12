#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 2: return 0
        intervals = sorted(intervals, key=lambda x:x[0])
        
        end_point = intervals[0][1]
        res = 0

        for x_start, x_end in intervals[1:]:
            if x_start < end_point:
                res += 1
                end_point = min(end_point, x_end)
            else:
                end_point = x_end
        return res

        # for i in range(1,len(intervals)):
        #     if end_point > intervals[i][0]:
        #         res += 1
        #         end_point = min(end_point, intervals[i][1])     # expand the interval
        #     else:
        #         # move to next end
        #         end_point = intervals[i][1]
        # return res

