#
# @lc app=leetcode id=84 lang=python
#
# [84] Largest Rectangle in Histogram
#
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        mono_stack = []     # indexes with ascending heights
        max_rect = 0
        
        # add 0 to the end so that all indexes in the stack will be checked
        for i, cur_height in enumerate(heights + [0]):
            # when cur_height < previous, then width increased
            while mono_stack and heights[mono_stack[-1]] >= cur_height:
                height = heights[mono_stack.pop()]              # convert index to height
                left = mono_stack[-1] if mono_stack else -1     # index to the left of the stack
                width = i - 1 - left
                rect = width * height       
                max_rect = max(max_rect, rect)
                
            # both width and height increased
            mono_stack.append(i)
        
        return max_rect

