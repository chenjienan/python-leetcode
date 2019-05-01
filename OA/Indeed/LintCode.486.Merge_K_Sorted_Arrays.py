import heapq

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        heap = []
        res = []

        # initialize the heap
        # add the first element of the arrays into heap
        for i, array in enumerate(arrays):
            if len(array) == 0: continue
            heapq.heappush(heap, (array[0], i, 0))  # (value, array_index, element_index)

        # this heap is always keeping x (x<k) elements
        while heap:
            val, array_i, elem_i = heapq.heappop(heap)
            res.append(val)

            # add one element from the current array
            if elem_i + 1 < len(arrays[array_i]):
                heapq.heappush(heap, (arrays[array_i][elem_i+1], array_i, elem_i + 1))

        return res

s = Solution()
r = s.mergekSortedArrays([
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ])

print(r)