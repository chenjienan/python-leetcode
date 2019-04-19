#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (34.25%)
# Total Accepted:    140.3K
# Total Submissions: 408.6K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
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
    def findOrder(self, numCourses: int, prerequisites):
        
        course_graph, in_degree = self.build_graph(numCourses, prerequisites)
        
        course_seq, q = [], []

        # find the first node
        for node in range(numCourses):
            if in_degree[node] == 0:
                q.append(node)

        while q:
            cur_node = q[0]
            course_seq.append(cur_node)
            # get all neighbours
            for node in course_graph[cur_node]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)

            q = q[1:]
        
        return course_seq if len(course_seq) == numCourses else []


    def build_graph(self, numCourses, prerequisites):
        edges = {e:[] for e in range(numCourses)}
        degree = [0 for d in range(numCourses)]

        # draw the dependency graph
        for node, edge in prerequisites:
            edges[edge].append(node)
            degree[node] += 1
        
        return edges, degree
s = Solution()
s.findOrder(2, [[1,0]])