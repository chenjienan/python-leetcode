#
# @lc app=leetcode id=460 lang=python
#
# [460] LFU Cache
#

import heapq
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.time = 0
        self.map = {}               # key to value
        self.freq_time = {}         # key to (freq, time) (for heap)
        self.priority_queue = []    # (freq, time, key), only updated when new key is added
        self.update = set()         # keys that have been get/put since last new key was added (for heap)


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.time += 1

        if key in self.map:
            
            freq, _ = self.freq_time[key]                # get frequency 
            self.freq_time[key] = (freq + 1, self.time)  # update frequency and time
            self.update.add(key)
            return self.map[key]
        
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity <= 0: return 
        
        self.time += 1
        if not key in self.map:
            
            if len(self.map) >= self.capacity:      # must remove least frequent from cache
                
                # update the heap
                while self.priority_queue and self.priority_queue[0][2] in self.update:
                    # whilst (least frequent, oldest) needs to be updated, update it and add back to heap
                    _, _, k = heapq.heappop(self.priority_queue)    # find key
                    f, t = self.freq_time[k]                        # update frequency and time
                    heapq.heappush(self.priority_queue, (f, t, k))  # push back
                    # this is used for udating and tracking all keys
                    self.update.remove(k)

                # 3 steps to remove (least frequent, oldest)
                _, _, k = heapq.heappop(self.priority_queue)
                self.map.pop(k)
                self.freq_time.pop(k)
            
            # add new key-value
            self.freq_time[key] = (0, self.time)
            heapq.heappush(self.priority_queue, (0, self.time, key))
            
        else:
            # same as get(key)
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time) 
            self.update.add(key)

        self.map[key] = value
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

