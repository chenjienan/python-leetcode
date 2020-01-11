def minDel(s):
    count_A = 0
    count_B = 0
    count_remove = 0

    for ch in s:
        if ch == 'A':
            count_A += 1
            if count_B > count_remove:
                count_remove += 1

        else:
            count_B += 1
            if count_A == 0:
                count_remove += 1

    return min(count_A, min(count_B, count_remove))

import collections
def minDel2(s):
    right = collections.Counter(s)
    left = collections.Counter()
    res = left['B'] + right['A']
    
    for c in s:
        left[c] += 1
        right[c] -= 1
        res = min(res, left['B'] + right['A'])
    return res

print(minDel2("BAAABAB"))