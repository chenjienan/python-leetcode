#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height: List[int]) -> int:
        # 反向双指针
        # each pos (index) = min(max_left, max_right) - cur_height

        if not height: return 0
        
        n = len(height)
        left, right = [height[0]], [height[-1]]
        water = 0

        # 从左到右扫描一边数组，获得每个位置往左这一段的最大值
        for i in range(1, n):
            # compare with the previous index
            left.append(max(left[i-1], height[i]))

        # 再从右到左扫描一次获得每个位置向右的最大值
        for j in range(1, n):
            # compare with the previous index from the right
            right.append(max(right[j-1], height[n-1-j]))
        right.reverse()

        # 可以用deque
        # for j in range(n-2, -1, -1):
        #     right.appendleft(max(height[j], right[0]))

        # 每个位置上的盛水数目 = min(左侧最高，右侧最高) - 当前高度
        for i in range(n):
            water += min(left[i], right[i]) - height[i]

        return water
        

