#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#
import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = collections.OrderedDict()
        self.cap = capacity
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            # val = self.dict[key]
            # self.dict.move_to_end(key) Python 3
            val = self.dict.pop(key)
            self.dict[key] = val
            return val
        return -1
            

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            # self.dict.move_to_end(key) Python 3
            self.dict.pop(key)
            self.dict[key] = value

        elif self.size < self.cap:
            self.dict[key] = value
            self.size += 1
        
        else:
            self.dict.popitem(last=False)
            self.dict[key] = value
            self.size += 1

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

