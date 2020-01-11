def largestInt(A):
    
    A.sort()
    left = 0
    right = len(A) - 1

    if A[left] > 0:
        return 0

    while left < right:
        if abs(A[left]) == A[right]:
            return A[right]
        elif abs(A[left]) > A[right]:
            left += 1
        else:
            right -= 1
    
    return 0

print(largestInt([3, 2, -2, 5, -3]))
print(largestInt([3, 2, -1, 5, -4]))
print(largestInt([3, 2, -99, 5, -4]))
print(largestInt([4, 2, 1, 5, -4]))
