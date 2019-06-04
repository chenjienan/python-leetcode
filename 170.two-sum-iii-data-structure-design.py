#
# @lc app=leetcode id=170 lang=python
#
# [170] Two Sum III - Data structure design
#
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.counter[number] = self.counter.get(number, 0) + 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for d1 in self.counter:
            d2 = value - d1        # get another value
            # self.counter[d1] == 1 only itself
            if d2 in self.counter and (d2 != d1 or self.counter[d1] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

