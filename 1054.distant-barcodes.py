#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        if n < 2: return barcodes
        
        dict = {}
        for d in barcodes:
            dict[d] = dict.get(d, 0) + 1
        
        heap = []
        for k, v in dict.items():
            heapq.heappush(heap, (-v, k))
        
        res = []
        while heap:
            if len(heap) >= 2:
                freq1, d1 = heapq.heappop(heap)
                freq2, d2 = heapq.heappop(heap)
                
                res.append(d1)
                res.append(d2)
                
                if -freq1 > 1: heapq.heappush(heap, (freq1 + 1, d1))
                if -freq2 > 1: heapq.heappush(heap, (freq2 + 1, d2))
                
            
            elif len(heap) == 1:
                freq, d = heapq.heappop(heap)
                res.append(d)
        
        return res 

