#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#

import collections 

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 我们需要一个数据结构来记录最大值和一些备选的值。
        # 考虑到这个滑动窗口，有FIFO的特性，考虑用deque
        # deque存 (index, value)
        dq = collections.deque()
        res = []
        
        for i, v in enumerate(nums):
            
            # 把当前小的顶出去
            # 单调双队列: 左值为当前窗口最大
            while dq and v > dq[-1][1]:
                dq.pop()
            #加入新值
            dq.append((i, v))

            # 窗口建立后输出数值
            if i + 1 >= k:
                res.append(dq[0][1])
            # 清除老值
            if i + 1 - dq[0][0] == k:
                dq.popleft()

        return res

            