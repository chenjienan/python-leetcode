def func(A, B, M):
    hash_map = {}

    for i in range(M):
        hash_map[A[i]] = hash_map.get(A[i], 0) + 1
        hash_map[B[i]] = hash_map.get(B[i], 0) + 1

    maxRank = 0
    for i in range(M):
        rank = hash_map[A[i]] + hash_map[B[i]] - 1 # -1 as the road is counted twice
        maxRank = max(maxRank, rank)
    
    return maxRank


print(func([1, 2, 3, 3], [2, 3, 1, 4], 4))