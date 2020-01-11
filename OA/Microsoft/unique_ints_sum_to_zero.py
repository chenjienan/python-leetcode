def uniqueInts(num):
    res = []
    if num % 2 == 1:
        res.append(0)
    val = num // 2   
    while val:
        res.append(val)
        res.append(-val)
        val -= 1
    return res 

print(uniqueInts(6))
print(uniqueInts(4))
print(uniqueInts(5))