

from collections import deque

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def infect(matrix):
    
    if not matrix:
        return -1;
        
    zombie_pos = deque()
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                zombie_pos.append((r, c))
    
    if not zombie_pos:
        return -1

    res = 0
    while zombie_pos:
        new_zombie_pos = deque()
        while zombie_pos:
            r, c = zombie_pos.popleft()
            for _r, _c in DIRECTIONS:
                nxt_r = r + _r
                nxt_c = c + _c

                if 0 <= nxt_r < rows and \
                    0 <= nxt_c < cols and \
                    matrix[nxt_r][nxt_c] != 1:
                    matrix[nxt_r][nxt_c] = 1
                    new_zombie_pos.append((nxt_r, nxt_c))

        if new_zombie_pos:
            zombie_pos = new_zombie_pos
        else:
            break
        res += 1
    
    return res


m = [
    [0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0]
]
print(infect(m))