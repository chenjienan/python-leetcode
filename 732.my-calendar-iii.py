#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#
class MyCalendarThree:
    
    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1
        
        active = res = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            
            if active > res:
                res = active
        
        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

