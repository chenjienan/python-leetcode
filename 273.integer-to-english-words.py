#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
class Solution:
    def numberToWords(self, num: int) -> str:
        if not num: return 'Zero'

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        res = ''
        if billion:        
            res = self.three_int(billion) + ' Billion'
        if million:
            res += ' ' if res else ''    
            res += self.three_int(million) + ' Million'
        if thousand:
            res += ' ' if res else ''
            res += self.three_int(thousand) + ' Thousand'
        if rest:
            res += ' ' if res else ''
            res += self.three_int(rest)
        return res

    def one_to_9(self, num):
        h = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return h[num]

    def ten_to_20(self, num):
        h = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return h[num]

    def tens(self, num):
        h = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return h[num]

    def two_int(self, num):
        if not num: return ''
        elif num < 10: return self.one_to_9(num)
        elif num < 20: return self.ten_to_20(num)
        else:
            tens = num // 10
            remain = num - tens * 10
            return self.tens(tens) + ' ' + self.one_to_9(remain) if remain else self.tens(tens)

    def three_int(self, num):
        hundred = num // 100
        remain = num - hundred * 100
        if hundred and remain:
            return self.one_to_9(hundred) + ' Hundred ' + self.two_int(remain)
        elif not hundred and remain:
            return self.two_int(remain)
        elif hundred and not remain:
            return self.one_to_9(hundred) + ' Hundred'

    


