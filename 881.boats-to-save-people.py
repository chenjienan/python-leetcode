#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        left = 0
        right = len(people) - 1
        count = 0
        
        while left <= right:
            if people[right] == limit:
                right -= 1
            
            # people[right] < limit
            else:
                if people[left] + people[right] <= limit:
                    left += 1
                    right -= 1
                else:
                    right -= 1
            count += 1
        
        return count
# @lc code=end

