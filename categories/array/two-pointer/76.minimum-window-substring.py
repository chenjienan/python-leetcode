#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        
        # two pointer - sliding window 
        # 同向双指针
        # ptr left: 设定窗口起始, minimize the window size
        # ptr right: 扩展现有的窗口大小 - find desirable window
        d = {}
        for c in t: d[c] = d.get(c, 0) + 1
        
        left, right = 0, 0
        num_unique_char_t, total_unique_char_t = 0, len(d)
        window_count = {}
        res = float('inf'), None, None      # (length, left, right)

        # right ptr to expand the window
        for right, ch_r in enumerate(s):
            # add cur char to the window
            window_count[ch_r] = window_count.get(ch_r, 0) + 1

            # found the unique char
            if ch_r in d and window_count[ch_r] == d[ch_r]: num_unique_char_t += 1
            
            # shrink the size until window is not desirable
            while left <= right and num_unique_char_t == total_unique_char_t:
                cur_len = right - left + 1
                if cur_len < res[0]: res = (cur_len, left, right)
                
                # remove char from the window
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in d and window_count[left_char] < d[left_char]: num_unique_char_t -= 1
                
                left += 1

        return "" if res[0] == float('inf') else s[res[1]: res[2]+1]
# 1. init two pointer
# 2. right ptr to expand the window until we get a "desirable" window
# 3. move left to shrink the size
# 4. until the window is not desirable, repeat step 2 onwards

s = Solution()
s.minWindow("ADOBECODEBANC", "ABC")