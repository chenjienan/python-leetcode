#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (37.26%)
# Total Accepted:    203.5K
# Total Submissions: 544.9K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        
        courses, in_degree = self.build_graph(numCourses, prerequisites)

        course_seq = []
        q = []

        for neighbour in range(numCourses):
            if in_degree[neighbour] == 0:
                q.append(neighbour)

        while q:
            cur_node = q[0]
            course_seq.append(cur_node)

            for neighbour in courses[cur_node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    q.append(neighbour)
            
            q = q[1:]
        
        return True if len(course_seq) == numCourses else False


    def build_graph(self, numCourses, prerequisites):
        # key: node
        # value: neighbours
        edges = {e:[] for e in range(numCourses)}
        # index: node
        # value: degree
        degrees = [0 for d in range(numCourses)]
        
        # create the relationship: add neighbours
        for node, edge in prerequisites:
            edges[edge].append(node)
            degrees[node] += 1

        return edges, degrees


s = Solution()
print(s.canFinish(2, [[1, 0]]))