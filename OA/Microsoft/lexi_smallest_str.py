def lexiSmallestStr1(s):
    if len(s) <= 1:
        return s
    
    res = ""
    cur = 0
    isRemoved = False

    while cur < len(s) - 1:
        if s[cur] > s[cur+1] and not isRemoved:
            isRemoved = True
        else:
            res += s[cur]
        cur += 1
    
    if not isRemoved:
        return res
    
    return res + s[cur]


def lexiSmallestStr2(s):
    if len(s) <= 1:
        return s

    isRemoved = False
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            isRemoved = True
            break

    if not isRemoved:
        return s[:-1]
    
    return s[:i] + s[i+1:]

print(lexiSmallestStr2("abczd"))
print(lexiSmallestStr2("abcde"))