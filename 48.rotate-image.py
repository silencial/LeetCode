#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - 2*i - 1):
                matrix[i][i+j], matrix[i+j][-i-1], matrix[-i-1][-i-j-1], matrix[-i-j-1][i] = \
                matrix[-i-j-1][i], matrix[i][i+j], matrix[i+j][-i-1], matrix[-i-1][-i-j-1]

# @lc code=end

