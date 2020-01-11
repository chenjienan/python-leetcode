def longestSubstr1(s):
    if len(s) < 3:
        return s
    
    start = 0
    end = len(s) - 1
    max_len = -float('inf')
    count = 0

    for i in range(len(s) - 1):
        count = 1   # count the occurance of the first char

        # check the char after i idx
        for j in range(i+1, len(s)):
            if s[j] == s[j-1]:
                count += 1
            else:
                count = 1   # reset counter

            if count == 3 or j == len(s) - 1:
                if max_len < j - i + 1: 
                    start = i
                    end = j - 1 if count == 3 else j
                    max_len = j - i + 1
                i = j - 2
                break

        if i == len(s) - 3:
            break

    return s[start, end+1]


# sliding window
def longestSubstr2(s):
    if len(s) < 3:
        return s
    
    cur = 0
    start = 0   # anchor pointer (expected to be the start idx of the substring)
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
                    start = cur     # set anchor pointer if length is max

            elif count > 2:
                cur = end - 1   #  reset cur pointer
        
        else:
            ch = s[end]
            count = 1

            if end - cur + 1 > max_len:
                max_len = end - cur + 1
                start = cur

        end += 1
    
    return s[start: start + max_len]


print(longestSubstr2("aabbaaaaabb"))
print(longestSubstr2("aabbaabbaabbaa"))