def maxValue(num):
    sign = 1

    if num < 0:
        # use reversed logic
        sign *= -1
        num *= -1

    num_ls = [int(x) for x in str(num)]
    i = 0
    while i < len(num_ls):
        if sign < 0 and num_ls[i] > 5:
            break
        if sign > 0 and num_ls[i] < 5:
            break
        i += 1
    
    num_ls = num_ls[:i] + [5] + num_ls[i:]
    return int(''.join(map(str, num_ls))) * sign

print(maxValue(268))
print(maxValue(670))
print(maxValue(0))
print(maxValue(-999))
print(maxValue(945))
print(maxValue(-439))