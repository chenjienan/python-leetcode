#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        sign = 1
        num = 0
        stack = []

        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)     # get the full number
            elif c in "-+":
                res += sign * num
                num = 0                     # reset to zero after calculation
                sign = 1 if c == '+' else -1
            elif c == '(':                  # prep for calculation
                stack.append(res)           # cache previous calculation in a stack
                stack.append(sign)          # cache the sign in a stack
                sign, res = 1, 0            # reset sign and res
            elif c == ')':
                res += sign * num
                res *= stack.pop()          # calulate the sign before parentheses
                res += stack.pop()          # A sign (B)
                num = 0                     # reset to zero after calculation

        return res + num * sign

