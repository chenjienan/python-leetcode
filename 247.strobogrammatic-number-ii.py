#
# @lc app=leetcode id=247 lang=python3
#
# [247] Strobogrammatic Number II

import collections

class Solution:
    def findStrobogrammatic(self, n: int):
        
        if n == 1: return ['0', '1', '8']
        # initialziation
        mapping = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        queue = collections.deque([])

        if n % 2 != 0: 
            queue.append("1")
            queue.append("0")
            queue.append("8")
        else:
            queue.append("")
        
        res = []

        while queue:
            cur_num = queue.popleft()

            if len(cur_num) == n:
                # 数首不可以是除非n是1
                if cur_num[0] != '0':
                    res.append(cur_num)
                    
            # stop adding item to the queue if length exceeded
            else:
                for k, v in mapping.items():
                    queue.append(k + cur_num + v)
        
        return res

s = Solution()
s.findStrobogrammatic(2)
        



