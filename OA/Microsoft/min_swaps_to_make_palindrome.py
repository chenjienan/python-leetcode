def canFormPalindrome(s):
    hash_set = set()

    for ch in s:
        if ch in hash_set:
            hash_set.remove(ch)
        else:
            hash_set.add(ch)
    
    return len(hash_set) < 2


def minSwapPalindrome(input_s):
    s = list(input_s)
    res = 0
    if (not canFormPalindrome(s)):
        return -1
    
    left = 0
    right = len(s) - 1

    while left < right:

        # find the next identical char if left right are not paired
        same_char_idx = right   # need the value of right later
        while s[left] != s[same_char_idx] and same_char_idx > left:
            same_char_idx -= 1
        
        # after finding the paird char idx, perform swap operation
        # and collect the steps
        if s[left] == s[same_char_idx] and left != same_char_idx:
            while same_char_idx < right:
                s[same_char_idx], s[same_char_idx+1] = s[same_char_idx+1], s[same_char_idx]
                same_char_idx += 1
                res += 1
            left += 1
            right -= 1
        # s[left] != s[same_char_idx] or left == same_char_idx
        # meaning found the single char that has no pair
        else:
            s[left], s[left+1] = s[left+1], s[left]
            res += 1

    return res

print(minSwapPalindrome("ntiin"))
print(minSwapPalindrome("aabb"))
print(minSwapPalindrome("asflkj"))
print(minSwapPalindrome("mamad"))