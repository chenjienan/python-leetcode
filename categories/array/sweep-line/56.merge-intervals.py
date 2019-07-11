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
        # sorting according to start time
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        # 做两件事: 保证在res里的元素符合条件
        # 1. 新增interval
        # 2. 扩展旧interval 如果又重叠
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            # add new interval
            # last end < cur start
            if res[-1][1] < cur_interval[0]:
                res.append(cur_interval)            
            # last end >= cur start
            else:
                # change exist interval (the last item of res)
                # expand exist interval end
                res[-1][1] = max(res[-1][1], cur_interval[1])
        return res

