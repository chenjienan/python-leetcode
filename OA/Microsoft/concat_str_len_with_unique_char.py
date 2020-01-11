import collections
def concat(arr):
    # key: str length
    # value: idx of the str
    hash_map = collections.defaultdict(list)
    for i, s in enumerate(arr):
        if len(set(s)) == len(s):       # exclude the string with duplicates
            hash_map[len(s)].append(i)

    ls = []
    # add the idx of the str in the list in desending order
    for size in sorted(hash_map, reverse=True):
        ls += hash_map[size]

    res = 0
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            idx1, idx2 = ls[i], ls[j]
            if not (set(arr[idx1]) & set(arr[idx2])):   # check if two strings have duplicates
                return len(arr[idx1]) + len(arr[idx2])
    return 0

def concat2(arr):
    
    str_ls = []
    for s  in arr:
        if len(set(s)) == len(s):
            str_ls.append(s)

    if len(str_ls) == 1:    # doen't need to concat
        return len(str_ls[0])

    max_len = 0
    for i in range(len(str_ls)):
        cur_str = str_ls[i]
        for j in range(i+1, len(str_ls)):
            concat_str = cur_str + str_ls[j]
            if len(set(concat_str)) == len(concat_str):
                max_len = max(max_len, len(concat_str))
                cur_str = concat_str

    return max_len


# print(concat2(["co","dil","ity"]))
# print(concat2(["abc","kkk","def","csv"]))
# print(concat2(["abc","ade","akl"]))
# print(concat2(["a","b","c"]))
# print(concat2(["a","a","a"]))
print(concat2(["abcdefghijklmnopqrstuvwxyz"]))