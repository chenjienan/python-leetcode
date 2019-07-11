#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()

        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        # return a list of words: recursion
        def words(n):
            if n < 20: return to19[n-1:n]
            if n < 100: return [tens[n//10 - 2]] + words(n % 10)
            if n < 1000: return [to19[n//100 - 1]] + ['Hundred'] + words(n % 100)
            
            # mapping:
            # p(power) w(word)
            # 1 Thousand
            # 2 Million
            # 3 Billion
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000 ** (p+1): return words(n // 1000 ** p) + [w] + words(n % 1000 ** p)

        return ' '.join(words(num)) or 'Zero'                

