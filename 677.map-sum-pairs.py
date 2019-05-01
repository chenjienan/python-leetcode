#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        cur_node = self.root
        for c in key:                        
            cur_node = cur_node.children[c]
        cur_node.count = val

    def sum(self, prefix: str) -> int:
        res = 0
        cur_node = self.root

        for c in prefix:
            if c not in cur_node.children: return 0
            cur_node = cur_node.children[c]
        
        # run dfs
        # sum of all the pairs' value whose key starts with the prefix
        stack = [cur_node]
        while stack:
            node = stack.pop()
            res += node.count
            stack.extend(node.children.values())

        return res
        
from collections import defaultdict
class TrieNode:
    # every node should have a counter
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

