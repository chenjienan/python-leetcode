#
# @lc app=leetcode id=681 lang=python
#
# [681] Next Closest Time
#
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = set([x for x in time if x in '1234567890'])
        
        hour, minute = time.split(':')
        
        # 从现在的时间每分钟递加
        while 1:
            # minute打头
            # handle overflow
            if minute == '59': 
                hour = str(int(hour) + 1)
                minute = '00'
            else:
                minute = str(int(minute) + 1)
            
            # handle overflow
            if int(hour) > 23:
                hour = '00'
            
            # 补零头
            if len(hour) == 1:
                hour = '0' + hour
            if len(minute) == 1:
                minute = '0' + minute

            # 确认时间是否在digits里面
            found = True
            for d in hour + minute:
                if d not in digits:
                    found = False
                    break

            if found: return hour + ':' + minute 
