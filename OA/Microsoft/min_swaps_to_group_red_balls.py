def minSwaps(s):
    red_count = 0
    for ch in s:
        if ch == 'R':
            red_count += 1

    if red_count == 1:
        return -1
    # two pointers
    left = 0
    right = len(s) - 1
    res = 0

    while left < right:
        if s[left] == 'R' and s[right] == 'R':
            red_count -= 2
            res += right - left - 1 - red_count  # distance between left and right without the red balls in between
            left += 1
            right -= 1
        elif s[left] != 'R':
            left += 1
        else:
            right -= 1  # s[left] == 'R' and s[right] != 'R'
    
    return res

print(minSwaps('WRRWWR'))
print(minSwaps('RRRWRR'))
print(minSwaps('WWRWWWRWR'))
print(minSwaps('WWW'))
print(minSwaps('RW'))