#
# @lc app=leetcode id=716 lang=python
#
# [716] Max Stack
#
class MaxStack(object):

    def __init__(self):
            """
            initialize your data structure here.
            """
            self.stack = []

    def push(self, x):
        m = max(x, self.stack[-1][1] if self.stack else None)
        self.stack.append((x, m))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def peekMax(self):
        return self.stack[-1][1]

    def popMax(self):
        m = self.stack[-1][1]
        b = []
        while self.stack[-1][0] != m:
            b.append(self.stack.pop()[0])

        self.pop()
        map(self.push, reversed(b))
        return m

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

