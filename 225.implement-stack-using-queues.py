#
# @lc app=leetcode id=225 lang=python
#
# [225] Implement Stack using Queues
#
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.q_helper = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        i = len(self.q)
        while i > 1:
            val = self.pop()
            self.q.append(val)
            i -= 1

        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.q: return None
        val = self.q[0]
        self.q = self.q[1:]
        return val

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.q: return self.q[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if self.q else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

