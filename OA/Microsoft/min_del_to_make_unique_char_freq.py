def minDeletion(s):
    if not s or len(s) < 2:
        return 0
    
    hash_map = {}
    for ch in s:
        hash_map[ch] = hash_map.get(ch, 0) + 1

    hash_set = set()
    count = 0
    for v in hash_map.values():
        while v > 0:
            if v not in hash_set:
                hash_set.add(v) 
                break
            count += 1
            v -= 1

    return count

print(minDeletion("eeeeffff"))
print(minDeletion("aabbffddeaee"))
print(minDeletion("llll"))
print(minDeletion("example"))