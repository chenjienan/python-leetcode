# input: array of nums
# output: integer (number of steps)

def pileEqualHeight(A):
    if not A or len(A) == 0:
        return A
    
    if len(A) < 2:
        return 0

    A.sort(reverse=True)
    res = 0
    diff = 1    # cache the difference
    pre_num = A[0]

    for i in range(1, len(A)):
        if A[i] != pre_num:
            res += diff
            pre_num = A[i]
        
        diff += 1
    
    return res


print(pileEqualHeight([5, 2, 1]))
