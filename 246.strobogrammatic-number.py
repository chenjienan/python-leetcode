#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        char_map = {'1':'1', '6':'9', '8':'8', '9':'6', '0':'0'}
        
        s_num = str(num)
        new_s = ''
        for ch in s_num:
            if ch not in char_map: return False
            
            new_s = char_map[ch] + new_s
        
        return s_num == new_s 

