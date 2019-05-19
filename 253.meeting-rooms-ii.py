#
# @lc app=leetcode id=253 lang=python
#
# [253] Meeting Rooms II
#
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        start, end = [], []

        for time in intervals:
            start.append(time[0])
            end.append(time[1])
        
        # 组建一个线性的关系, 构建人进房间的模型
        start.sort()
        end.sort()
        

        cnt = 0
        left = 0    # 为end time设定的一个left pointer
        for i in range(len(intervals)):
            if start[i] < end[left]: cnt += 1
            else: left += 1
        return cnt
