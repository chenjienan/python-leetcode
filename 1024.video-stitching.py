#
# @lc app=leetcode id=1024 lang=python
#
# [1024] Video Stitching
#
class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        clips.sort(key=lambda x: (x[0], x[1]))    
        right = 0    
        idx = 0
        count = 0
        
        while idx < len(clips) :
            if clips[idx][0] > right: return -1
            
            farReach = right
            while idx < len(clips) and clips[idx][0] <= right: 
                farReach = max(farReach, clips[idx][1])
                idx += 1
            
            right = farReach
            count += 1
                            
            if farReach >= T: return count

        return -1

