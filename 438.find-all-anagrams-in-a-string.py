#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # cnt = collections.Counter(p)
        # len_p = len(p)
        # res = []
        # for i in range(len(s) - len_p + 1):
        #     sub_str = s[i:i+len_p]
        #     sub_str_cnt = collections.Counter(sub_str)
        #     if cnt == sub_str_cnt: res.append(i)
        # return res

        dic1, dic2 = dict(), dict()
        for each in p:
            dic1[each] = dic1.get(each,0) + 1
        start, end = 0, 0
        res = []
        
        while end < len(s):
            dic2[s[end]] = dic2.get(s[end],0) + 1
            if dic1 == dic2:
                res.append(start)
            
            end += 1
                
            # compare
            if end -start + 1 > len(p):
                dic2[s[start]] -= 1
                if dic2[s[start]] == 0:
                    del(dic2[s[start]])
                start += 1
        return res

