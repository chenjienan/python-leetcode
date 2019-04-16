#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#
# https://leetcode.com/problems/friend-circles/description/
#
# algorithms
# Medium (53.10%)
# Total Accepted:    80.5K
# Total Submissions: 151.5K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 
# There are N students in a class. Some of them are friends, while some are
# not. Their friendship is transitive in nature. For example, if A is a direct
# friend of B, and B is a direct friend of C, then A is an indirect friend of
# C. And we defined a friend circle is a group of students who are direct or
# indirect friends.
# 
# 
# 
# Given a N*N matrix M representing the friend relationship between students in
# the class. If M[i][j] = 1, then the ith and jth students are direct friends
# with each other, otherwise not. And you have to output the total number of
# friend circles among all the students.
# 
# 
# Example 1:
# 
# Input: 
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a
# friend circle. The 2nd student himself is in a friend circle. So return 2.
# 
# 
# 
# Example 2:
# 
# Input: 
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd
# students are direct friends, so the 0th and 2nd students are indirect
# friends. All of them are in the same friend circle, so return 1.
# 
# 
# 
# 
# Note:
# 
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.
# 
# 
#
class Solution:
    def findCircleNum(self, M):
        row = len(M)
        col = len(M[0])
        res = row
        uf = UnionFindSet(row)
        # print(uf.father)
        for i in range(row):
            for j in range(col):
                if M[i][j] == 1 and not uf.query(i, j):
                    uf.union(i, j)
                    res -= 1        
        return res


class UnionFindSet:

    def __init__(self, n):
        self.father = {}

        for i in range(n):
            self.father[i] = i
    
    def union(self, a, b):
        root_x = self.find(a)
        root_y = self.find(b)
        self.father[root_x] = self.father[root_y]
    
    def query(self, a, b):
        return self.find(a) == self.find(b)
    
    def find(self, node):
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]

        for p in path:
            self.father[p] = node
        
        return node


# s = Solution()
# M = [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# print(s.findCircleNum(M))