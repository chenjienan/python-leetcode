def rule_1(s_num):
    score = 0
    for c in s_num:
        if c == '7':
            score += 5
    return score

def rule_2(s_num):
    score = 0
    for i in range(len(s_num) - 1):
        if s_num[i:i+2] == '22':
            score += 6
    return score

def rule_3(s_num):
    score = 0
    count = 1
    ls_num = [int(x) for x in s_num]
    for i in range(len(ls_num)-1):
        if ls_num[i] - 1== ls_num[i+1]:
            count += 1
        else:
            score += count ** 2
            count = 1
            
    score += count ** 2
    return score

def rule_4(num):
    return 4 if num % 3 == 0 else 0

def rule_5(s_num):
    score = 0
    ls_num = [int(x) for x in s_num]
    for num in ls_num:
        if num % 2 == 0:
            score += 3
    return score

def main(num):
    s_num = str(num)
    res_1 = rule_1(s_num)
    res_2 = rule_2(s_num)
    res_3 = rule_3(s_num)
    res_4 = rule_4(num)
    res_5 = rule_5(s_num)
    return res_1 + res_2 + res_3 + res_4 + res_5
    
num = 765
print(main(num))