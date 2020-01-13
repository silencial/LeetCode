#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]:
            return 0

        for i in range(1, m):
            if obstacleGrid[i][0]:
                for j in range(i, m):
                    obstacleGrid[j][0] = 0
                break
            obstacleGrid[i][0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i]:
                for j in range(i, n):
                    obstacleGrid[0][j] = 0
                break
            obstacleGrid[0][i] = 1

        obstacleGrid[0][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 0
                    continue
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]

# @lc code=end
