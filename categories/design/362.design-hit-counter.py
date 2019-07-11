#
# @lc app=leetcode id=362 lang=python
#
# [362] Design Hit Counter
#
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = collections.deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        # Use deque as container. Deque stores the value of the timestamp.
        self.counter.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        # 5 MINUTES = 5 * 60 = 300 seconds
        while self.counter and timestamp - self.counter[0] >= 300:
            self.counter.popleft()
        return len(self.counter)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

