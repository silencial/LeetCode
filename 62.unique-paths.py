#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    # O(mn) space
    # def uniquePaths(self, m: int, n: int) -> int:
    #     board = [([1] + [0] * (n - 1)) for i in range(m)]
    #     board[0] = [1] * n
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             board[i][j] = board[i - 1][j] + board[i][j - 1]
    #     return board[-1][-1]

    # O(min(m, n)) space
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = max(m, n), min(m, n)
        row = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[-1]

# @lc code=end
