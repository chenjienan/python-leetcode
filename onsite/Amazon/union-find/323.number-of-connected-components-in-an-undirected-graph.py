#
# @lc app=leetcode id=323 lang=python
#
# [323] Number of Connected Components in an Undirected Graph
#
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])
        
        return uf.cap

class UnionFind:

    def __init__(self, n):
        self.cap = n
        self.father = {}
        for i in range(n):
            self.father[i] = i  # I am the boss of myself
        
    def union(self, a, b):
        boss_a = self.find(a)
        boss_b = self.find(b)
        if boss_a == boss_b: return     # already connected
        self.father[boss_a] = self.father[b]
        self.cap -= 1

    def find(self, node):
        path = []
        
        # find the big boss
        while self.father[node] != node: # not equals to itself
            path.append(node)
            node = self.father[node]
        
        # path compression
        for item in path:
            self.father[item] = node

        return node

    # def query(self, a, b):
    #     return self.find(a) == self.find(b)
