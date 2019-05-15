#
# @lc app=leetcode id=746 lang=python
#
# [746] Min Cost Climbing Stairs
#
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n < 3: return min(cost)
        dp = [0] * (n)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i] 
        
        # min cost to reach the top
        return min(dp[-1], dp[-2])


s = Solution()
s.minCostClimbingStairs([0,0,0,1])