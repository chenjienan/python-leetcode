#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        char_dict = {}
        for ch in ransomNote:
            char_dict[ch] = char_dict.get(ch, 0) + 1
        
        for ch in magazine:
            if ch in char_dict:
                char_dict[ch] -= 1
                
                if char_dict[ch] == 0:
                    del char_dict[ch]
            
        return False if char_dict else True

