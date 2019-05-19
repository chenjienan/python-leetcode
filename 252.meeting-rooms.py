#
# @lc app=leetcode id=252 lang=python
#
# [252] Meeting Rooms
#
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        start = []
        end = []

        for time in intervals:
            start.append(time[0])
            end.append(time[1])

        start.sort()
        end.sort()
        # 一个人出房间之前,又一个人进来
        for i in range(1, len(intervals)):
            if start[i] < end[i-1]:
                return False
        return True 
