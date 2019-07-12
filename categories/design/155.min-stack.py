#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # store tuples: (cur_val, min_val)
        # 把current min放到每个值里
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # key point of this problem
        cur_min = self.getMin()
        # 每次push做一次比较
        if cur_min == '#' or cur_min > x: cur_min = x
        new_item = (x, cur_min)
        self.stack.append(new_item)


    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack = self.stack[:-1]

    def top(self):
        """
        :rtype: int
        """
        val = self.stack[-1][0]
        return val

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack: return self.stack[-1][1]
        return '#'


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

