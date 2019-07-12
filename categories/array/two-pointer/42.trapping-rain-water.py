#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height: List[int]) -> int:
        # 方向双指针
        # each pos (index) = min(max_left, max_right) - cur_height

        if not height: return 0
        
        n = len(height)
        left, right = [height[0]], [height[-1]]
        water = 0

        for i in range(1, n):
            # compare with the previous index
            left.append(max(left[i-1], height[i]))

        for i in range(1, n):
            # compare with the previous index from the right
            right.append(max(right[i-1], height[n-1-i]))
        right.reverse()

        for i in range(n):
            water += min(left[i], right[i]) - height[i]

        return water
        

