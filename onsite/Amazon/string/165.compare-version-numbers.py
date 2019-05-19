#
# @lc app=leetcode id=165 lang=python
#
# [165] Compare Version Numbers
#
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list = version1.split('.')
        v2_list = version2.split('.')

        for i in range(max(len(v1_list), len(v2_list))):
            v1 = int(v1_list[i]) if len(v1_list) > i else 0
            v2 = int(v2_list[i]) if len(v2_list) > i else 0
            if v1 > v2: return 1
            elif v1 < v2: return -1
            # if v1 == v2, next round 
        return 0
        

