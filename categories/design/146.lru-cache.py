#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#
# import collections

# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.dict = collections.OrderedDict()
#         self.cap = capacity
#         self.size = 0

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key in self.dict:
#             # val = self.dict[key]
#             # self.dict.move_to_end(key) Python 3
#             val = self.dict.pop(key)
#             self.dict[key] = val
#             return val
#         return -1
            

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if key in self.dict:
#             # self.dict.move_to_end(key) Python 3
#             self.dict.pop(key)
#             self.dict[key] = value

#         elif self.size < self.cap:
#             self.dict[key] = value
#             self.size += 1
        
#         else:
#             self.dict.popitem(last=False)
#             self.dict[key] = value
#             self.size += 1

import collections
class LRUCache(object):
    """
    LRU with lazy loading strategy
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.CAP = capacity
        self.size = 0
        self.data = {}                          # store client's key-value pairs
        self.dq = collections.deque([])         # track the order of the Keys left(least use)
        self.update_history = {}                # track the actions of the update        
        
    def get(self, key):
        if key not in self.data:
            return -1
        
        # update key order
        # 预处理key 的update
        self.update_history[key] = self.update_history.get(key, 0) + 1
        self.dq.append(key)
        return self.data[key]
    

    def put(self, key, value):
        if key not in self.data:
            if self.size < self.CAP:
                self.size += 1
            
            else:
                old_key = self.dq.popleft()
                # 检查所有update的记录, 并找到least-used key
                # dq 与 update_history 一一对应
                while self.update_history.get(old_key, 0) > 0:
                    self.update_history[old_key] -= 1
                    old_key = self.dq.popleft()

                # 在cache中删除当前least-used Key
                self.data.pop(old_key)      
            
            
            self.data[key] = value
            self.dq.append(key)

        # key in cache
        else:
            self.data[key] = value
            # update key order
            self.update_history[key] = self.update_history.get(key, 0) + 1
            self.dq.append(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

