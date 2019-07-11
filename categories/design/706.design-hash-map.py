#
# @lc app=leetcode id=706 lang=python
#
# [706] Design HashMap
#
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 10000
        # buckets[0] => store key
        # buckets[1] => store value
        # and we have k buckets
        self.buckets = [[[], []] for _ in range(self.cap)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        bucket, idx = self._index(key)
        # add if not exists
        if idx == -1:
            bucket[0].append(key)
            bucket[1].append(value)
        # modify if exists
        else:
            bucket[0][idx] = key
            bucket[1][idx] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket, idx = self._index(key)
        if idx == -1: return -1        
        return bucket[1][idx]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        bucket, idx = self._index(key)
        if idx == -1: return None
        
        bucket[0].pop(idx)
        bucket[1].pop(idx)

    
    # need a hash function
    def _hash(self, key):
        return key % self.cap

    # find index
    def _index(self, key):
        h = self._hash(key)
        bucket = self.buckets[h]
        
        # bucket[0] stores keys
        for i, k in enumerate(bucket[0]):
            if k == key: return (bucket, i)
        return bucket, -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

