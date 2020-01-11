def maxInsert(s):
    if not s or len(s) == 0:
        return 2
    
    res = 0
    count = 0
    s = 'X' + s + 'X'   # can insert a before and after
    for i in range(len(s) - 1):
        if s[i] == 'a':
            count += 1
            if s[i+1] != 'a' and count < 2:
                res += 1
        
        if s[i] != 'a':
            count = 0
            if s[i+1] != 'a':
                res += 2

        if count > 2:
            return -1

    return res


print(maxInsert("aaba"))
print(maxInsert("aa"))
print(maxInsert("dog"))
print(maxInsert("baaaa"))
print(maxInsert("aabab"))