#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        "小放大， 大放小"
        self.minheap = []
        self.maxheap = []
    
    def addNum(self, num: int) -> None:
        
        # 以大堆头做reference
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        self.balance()
        
    def balance(self):
        l = len(self.minheap)
        r = len(self.maxheap)
        
        if l > r: heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))      
        # make sure r has 1 more element than l
        elif l + 1 < r: heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))


    def findMedian(self) -> float:
        l = len(self.minheap)
        r = len(self.maxheap)
        
        if l == r: return (self.minheap[0] - self.maxheap[0]) / 2.0  
        return float(-self.maxheap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

