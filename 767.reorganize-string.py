#
# @lc app=leetcode id=767 lang=python
#
# [767] Reorganize String
#
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        d = {}
        for c in S:
            d[c] = d.get(c, 0) + 1
        
        ordered_d = collections.OrderedDict(sorted(d.items(), key=lambda x:x[1]))
        # print(ordered_d)
        
        # put the most occurance char up front
        collection = []
        for k, v in ordered_d.items():
            if v > (len(S) + 1) // 2: return ""
            collection.extend(k * v)
            
        res = [None] * len(S)
        res[::2] = collection[len(S)//2:]
        res[1::2] = collection[:len(S)//2]
        
        return "".join(res) 

