# merge files, 给一个array [6 7 8 9], 每次merge两个，求最少的merge cost, 
# 要仔细看题啊，不是之前的lc1000 merge stones那题， 不需要连续的。

# test case 1
# numberOfSubFiles = 4
# files = [8, 4, 6, 12]

# test case 2
# numberOfSubFiles = 4
# files = [20, 4, 8, 2]

# test case 3
numberOfSubFiles = 6
files = [1, 2, 5, 10, 35, 89]

def minimumTime(numberOfSubFiles, files):
    
    f = files
    res = 0

    import heapq
    heapq.heapify(f)

    while len(f) >= 2:
        file_x = heapq.heappop(f)        
        file_y = heapq.heappop(f)
        merged_file = file_x + file_y
        heapq.heappush(f, merged_file)
        res += merged_file
        
    return res

print(minimumTime(numberOfSubFiles, files))