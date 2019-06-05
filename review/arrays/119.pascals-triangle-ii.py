#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [[1] * (i + 1) for i in range(rowIndex+1)]

        for i in range(rowIndex+1):
            # skip the first item [0] and last item [i]
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[-1]

s = Solution()
s.getRow(6)