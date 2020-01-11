def getDigitSum(num):
    sum = 0
    while num:
        sum += num % 10
        num // 10

# return the max sum of two numbers in an array, whose digits add up to an equal sum
# algorithm:
# scan the array, store the numbers whose digits add up to an equal sum in a hash map
# if one number has the same digit sum, update the max value and store the larger value in the map
def maxDigitSum(arr):
    # key: digit sum
    # value 
    hash_map = {}
    res = -1        # store the max value of a pair
    
    for num in arr:
        digit_sum = getDigitSum(num)
        if digit_sum in hash_map:
            last_num = hash_map[digit_sum]
            res = max(res, num + last_num)
            hash_map[digit_sum] = max(last_num, num)

        else:
            hash_map[digit_sum] = num

    return res