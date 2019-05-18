#
# @lc app=leetcode id=957 lang=python
#
# [957] Prison Cells After N Days
#
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        # transform list to string, so that
        # we can record all states in hashtable
        str_cells = str(cells)
        h = {str_cells: N}      # key: state, value i-th day

        while N > 0:            
            h.setdefault(str(cells), N)
            N -= 1
            middle_cells = [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1, 7)]
            cells = [0] + middle_cells + [0] 

            # key of this problem
            # 2^6 = 64 different states
            if str(cells) in h: N %= h[str(cells)] - N
        
        return cells
        

