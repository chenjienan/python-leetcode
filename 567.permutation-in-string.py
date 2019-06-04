#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
class Solution:
    def checkInclusion(self, s1: str, s2: str):
        # cnt_1 = collections.Counter(s1)
        cnt_1 = {}
        for s in s1: cnt_1[s] = cnt_1.get(s, 0) + 1
        len_s1 = len(s1)

        for i in range(len(s2) - len_s1 + 1):
            sub_str = s2[i: i + len_s1]
            cnt_2 = collections.Counter(sub_str)
            if cnt_1 == cnt_2:
                return True
        
        return False

