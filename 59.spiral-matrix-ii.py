#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    # def generateMatrix(self, n: int) -> List[List[int]]:
    #     matrix = [[0] * n for _ in range(n)]
    #     top = left = 0
    #     bot = right = n
    #     a = 1
    #     while top < bot and left < right:
    #         for i in range(left, right):
    #             matrix[top][i] = a
    #             a += 1
    #         top += 1
    #         for i in range(top, bot):
    #             matrix[i][right - 1] = a
    #             a += 1
    #         right -= 1
    #         if top < bot:
    #             for i in range(right - 1, left - 1, -1):
    #                 matrix[bot - 1][i] = a
    #                 a += 1
    #             bot -= 1
    #         if left < right:
    #             for i in range(bot - 1, top - 1, -1):
    #                 matrix[i][left] = a
    #                 a += 1
    #             left += 1
    #     return matrix

    # def generateMatrix(self, n):
    #     A = [[0] * n for _ in range(n)]
    #     i, j, di, dj = 0, 0, 0, 1
    #     for k in range(n * n):
    #         A[i][j] = k + 1
    #         if A[(i + di) % n][(j + dj) % n]:
    #             di, dj = dj, -di
    #         i += di
    #         j += dj
    #     return A

# @lc code=end
