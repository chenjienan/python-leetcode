#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        # s = set(secret)
        # cannot use set
        # we need to track the number of cows
        # if the same value presents
        s = {}
        for d in secret:
            if d not in s:
                s[d] = 1
            else:
                s[d] += 1

        bull_pos = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
                bull_pos.append(i)
                s[guess[i]] -= 1

        for i, d in enumerate(guess):
            if d in s and s[d] > 0 and i not in bull_pos:
                cow += 1
                s[d] -= 1

        return '{}A{}B'.format(bull, cow)


# secret = "1807"
# guess = "7810"

# secret = "1123"
# guess = "0111"
# s = Solution()
# print(s.getHint(secret, guess))