def func(s):
    if not s or len(s) < 3:
        return s

    res = s[0]
    count = 1
    i = 1
    while i < len(s):
        if s[i] == res[-1]:
            count += 1
        else:
            count = 1
        
        if count < 3:
            res += s[i]

        i += 1

    return res
    
print(func("eedaaad"))
print(func("xxxtxxx"))
print(func("uuuuxaaaaxuuu"))