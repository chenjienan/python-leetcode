#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
import heapq
class Solution:

    def kthSmallest(self, matrix, k):

        rows = cols = len(matrix)

        heap = []
        r, c = 0, 0
        visited = set((r, c))
        heapq.heappush(heap, (matrix[r][c], (r, c)))

        while k > 0:
            res, (r, c) = heapq.heappop(heap)

            if r + 1 < rows and (r+1, c) not in visited:
                heapq.heappush(heap, (matrix[r+1][c], (r+1, c)))
                visited.add((r+1, c))
            
            if c + 1 < cols and (r, c+1) not in visited:
                heapq.heappush(heap, (matrix[r][c+1], (r, c+1)))
                visited.add((r, c+1))

            k -= 1

        return res

s = Solution()
s.kthSmallest(
    [[1,5,9],[10,11,13],[12,13,15]],
    8
)
