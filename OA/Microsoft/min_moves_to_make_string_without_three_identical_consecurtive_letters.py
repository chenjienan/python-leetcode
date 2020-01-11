def func1(s):
    res = 0
    i = 0
    while i < len(s) - 2:
        if s[i] == s[i+1] and s[i+1] == s[i+2]:
            res += 1
            i += 2
        i += 1

    return res

# create a window (size is 3), then scan through the string with this window
# if we see 3 consecutive chars, increment the res.
def func2(s):
    res = 0
    i = 0
    while i < len(s) -2:
        window = s[i:i+3]
        if window == 'aaa' or window == 'bbb':
            res += 1
            i += 2
        i += 1
    return res 

print(func1("baaaaa"))
print(func1("baaabbaabbba"))
print(func1("baabab"))

print(func2("baaaaa"))
print(func2("baaabbaabbba"))
print(func2("baabab"))