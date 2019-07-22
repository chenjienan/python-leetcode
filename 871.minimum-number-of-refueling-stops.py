#
# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        cur_fuel = startFuel
        cur_id = 0
        count = 0
        stations += [[target, 0]]
        heap = []        # should use max heap
        
            
        while cur_id < len(stations):    
            if cur_fuel >= stations[cur_id][0]:
                heapq.heappush(heap, -stations[cur_id][1])             # 已经经过了，但没有用到它的油
                cur_id += 1
                    
            else:    # 不够油，需要吃后悔药
                while heap and cur_fuel < stations[cur_id][0]    :    # 到达下个油站
                    cur_fuel += -heapq.heappop(heap)                  # 虚拟加油
                    count += 1
            
                if cur_fuel < stations[cur_id][0] and not heap: return -1
        
        return count

