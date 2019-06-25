#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#

import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]):
        
        courses.sort(key=lambda x: x[1])
        day = 0
        heap = []
        for i in range(len(courses)):
            
            if day + courses[i][0] <= courses[i][1]:
                day += courses[i][0]
                heapq.heappush(heap, -courses[i][0])
            else:
                # has overlap
                heapq.heappush(heap, -courses[i][0])
                day += courses[i][0] + heap[0]
                heapq.heappop(heap)
        
        return len(heap)

