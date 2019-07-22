#
# @lc app=leetcode id=324 lang=python
#
# [324] Wiggle Sort II
#
class Solution(object):
    def wiggleSort(self, A):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if not A: return []

        n = len(A)
        median = self.find_kth(A, 0, n - 1, n // 2)

        i = 0
        odd = 1
        even = n - 1 if (n-1) % 2 == 0 else n - 2

        while i <= n-1:
            if A[i] > median and (i % 2 != 1 or odd < i):
                A[odd], A[i] = A[i], A[odd]
                odd += 2
                continue
            
            if A[i] < median and (i % 2 != 0 or even > i):
                A[even], A[i] = A[i], A[even]
                even -= 2
                continue

            i += 1
        
        return A

    
    def find_kth(self, A, start, end, k):
        left, right = start, end
        pivot = A[(left + right) // 2]

        while left <= right: 
            while left <= right and A[left] < pivot:
                left += 1
            
            while left <= right and A[right] > pivot:
                right -= 1
            
            if left <= right:
                A[left], A[right] = A[right], A[left]
                right -= 1
                left += 1
        
        if start <= k - 1 <= right:
            return self.find_kth(A, start, right, k)
        elif left <= k -1 <= end:
            return self.find_kth(A, left, end, k)
        else:
            return A[k-1]
