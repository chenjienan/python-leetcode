#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        # corner case with numerater = 0
        if  n == 0: 
            return "0"
        
        # corner cases with sign
        sign = 1
        if n < 0:
            sign *= -1
            n = abs(n)
            
        if d < 0:
            sign *= -1
            d = abs(d)
            
        if sign == -1:
            res = "-"
        else:
            res = ""
            
        # key: reminder * 10 value: pos
        hash_map = {}
        isRecurring = False
        
        # corner case with r == 0
        q, r = divmod(n, d)
        if r == 0:
            res += str(q)
            return res
        
        res += str(q) + '.'  
        decimal = []
        
        while r != 0:                       
            if r in hash_map:               
                isRecurring = True
                break
            hash_map[r] = len(hash_map)     # get all decimal by * 10 to reminder (r)
            q, r = divmod(r*10, d)          # next decimal number is r * 10 / numerator (add to res)
            decimal.append(str(q))
        
        # case for recurring decimals
        if isRecurring:
            decimal.insert(hash_map[r], '(')
            decimal.append(')')
        
        # general cases
        res += "".join(decimal)
        return res
# @lc code=end

