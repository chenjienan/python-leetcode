#
# @lc app=leetcode id=232 lang=python
#
# [232] Implement Queue using Stacks
#
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # two stacks
        # when pop, move n-1 to helper stack
        # pop the last element
        # push back to stack from helper stack
        self.stack = []
        self.stack_helper = []
        self.front = None
        self.size = 0


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if not self.front: self.front = x
        self.stack.append(x)
        self.size += 1
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack: return 
        
        cnt = self.size
        while cnt > 1:
            self.stack_helper.append(self.stack.pop())
            cnt -= 1
        
        self.front = self.stack_helper[-1] if self.stack_helper else None
        val = self.stack.pop()
        while self.stack_helper:
            self.stack.append(self.stack_helper.pop())
        self.size -= 1
        return val
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack: return
        return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return False if self.stack else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

