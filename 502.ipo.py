#
# @lc app=leetcode id=502 lang=python
#
# [502] IPO
#
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        ls = zip(Profits, Capital)
        ls.sort(key=lambda x: x[1])
        import heapq
        heap = []
        count = 0
        i = 0
        while count < k:
            while i < len(ls) and ls[i][1] <= W:
                heapq.heappush(heap, -ls[i][0])
                i += 1

            if heap:
                W += -heapq.heappop(heap)
                count += 1
            else:
                break
        return W
        

