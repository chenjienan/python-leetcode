def longestSemiAlterSubstr(s):
    if not s or len(s) == 0:
        return 0
        
    if len(s) < 3:
        return len(s)
    
    cur = 0
    end = 1     # look-ahead pointer
    ch = s[0]
    count = 1   # count the occurance of the first char
    max_len = 1

    while end < len(s):
        if s[end] == ch:
            count += 1

            if count == 2:
                if end - cur + 1 > max_len:
                    max_len = end - cur + 1

            elif count > 2:
                cur = end - 1   #  reset cur pointer
        
        else:
            ch = s[end]
            count = 1

            if end - cur + 1 > max_len:
                max_len = end - cur + 1

        end += 1
    
    return max_len

print(longestSemiAlterSubstr("baaabbabbb"))
print(longestSemiAlterSubstr("abaaaa"))