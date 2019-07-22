#
# @lc app=leetcode id=228 lang=python
#
# [228] Summary Ranges
#
class Solution(object):
    def summaryRanges(self, A):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not A: return []
        res = []
        start = end = cnt = A[0]
        for d in A[1:]:

            if cnt + 1 == d:
                cnt += 1
                end = d
            else:
                if end <= start:
                    res.append("{}".format(start))
                else:
                    res.append("{}->{}".format(start, end))
                start = d
                cnt = d

        if end <= start:
            res.append("{}".format(start))
        else:
            res.append("{}->{}".format(start, end))
            
        return res

