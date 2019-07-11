#
# @lc app=leetcode id=705 lang=python
#
# [705] Design HashSet
#
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 10000
        self.buckets = [[] for _ in range(self.cap)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket, index = self._index(key)
        # cannot find it
        if index == -1: bucket.append(key)
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket, index = self._index(key)
        if index >= 0: bucket.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        _, index = self._index(key)
        return index >= 0

    # need a hash function
    def _hash(self, key):
        return key % self.cap

    # find index
    def _index(self, key):
        h = self._hash(key)
        bucket = self.buckets[h]
        
        for i, v in enumerate(bucket):
            if v == key: return (bucket, i)
        return bucket, -1

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

