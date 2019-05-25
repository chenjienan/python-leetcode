#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1: return 0
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        # init
        # 坐标型DP, 2维数组即坐标
        f = [[0] * (cols) for _ in range(rows)]
        f[0][0] = 1
        
        # 初始化第二部: 第一列打竖走
        for i in range(1, rows):
            if obstacleGrid[i][0] == 1:
                break
            f[i][0] = 1
        
        # 初始化第三部: 第一行打横走
        for i in range(1, cols):
            if obstacleGrid[0][i] == 1:
                break
            f[0][i] = 1
        
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 0: 
                    # 从左面来 f[r][c-1], 或者从上面来 f[r-1][c]
                    f[r][c] = f[r-1][c]+f[r][c-1]
        
        return f[-1][-1]

# follow up：要是能走的方向改为 上、下、右，原先代码怎么改？
# 如果用户做查询时设定的robot能走的方向一直在变，怎么改这个
# 函数去适应这个需求（把可以走的方向变成参数传到函数里就行了）