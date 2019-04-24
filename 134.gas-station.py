#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost): return -1

        pos = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # only if there is one i the tank > 0 after circulate to the end
            if tank < 0:
                # cannot be reach, so reset
                tank = 0
                pos = i + 1
        
        return pos
