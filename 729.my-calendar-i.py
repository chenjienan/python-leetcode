#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#
class MyCalendar:
    
    def __init__(self):
        self.ls = []
        
    def book(self, start: int, end: int) -> bool:
        
        for s, e in self.ls:
            if start < e and end > s: return False
        
        self.ls.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

