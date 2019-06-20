#
# @lc app=leetcode id=373 lang=python
#
# [373] Find K Pairs with Smallest Sums
#
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        rows = len(nums1)
        cols = len(nums2)
        if rows == 0 or cols == 0: return []

        M = []
        for r in range(rows):
            ls = []
            for c in range(cols):
                ls.append(nums1[r] + nums2[c])
            M.append(ls)

        left = M[0][0]
        right = M[rows-1][cols-1]
 
        while left < right:
            mid = left + (right - left) // 2

            if self.equalOrSamller(M, mid) < k:
                left = mid + 1
            
            else:
                right = mid
        
        res = []
        x = left
        r = rows - 1
        c = 0
        while r >= 0 and c < cols:
            if M[r][c] <= x:
                for i in range(r, -1, -1):
                    res.append([nums1[i], nums2[c]])
                c += 1
            else:
                r -= 1
        
        res.sort(key=lambda x : x[0] + x[1])
        return res[:k] if k < len(res) else res

    # 有多少个小于等于X的元素
    def equalOrSamller(self, M, x):
        rows = len(M)
        cols = len(M[0])
        count = 0
        r, c = rows - 1, 0 # bot-left corner
        while r >= 0 and c < cols:
            if M[r][c] <= x:
                count += r + 1
                c += 1
            
            else:
                r -= 1
        return count

s = Solution()
s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
