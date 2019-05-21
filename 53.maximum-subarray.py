#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = 0
        # minvalue初始值为0因为如果只有一个值，那这个array最大值为这个值本身
        min_sum = 0
        max_sum = nums[0]   # or -float('inf')

        # 计算每个位置为结尾的 subarray 的最大值是多少
        for d in nums:
            prefix_sum += d
            # 先更新max再更新min，因为subarray自己减去自己的空sub情况不考虑在内
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum
        
        # # Solution #2
        # max_sum = local_max_sum = nums[0]
        
        # for i in range(1, len(nums)):
        #     local_max_sum = nums[i] + max(0, local_max_sum)
        #     max_sum = max(max_sum, local_max_sum)
            
        # return max_sum

