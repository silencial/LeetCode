#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    # Math
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - 2*i - 1):
                matrix[i][i + j], matrix[i + j][~i], matrix[~i][~(i + j)], matrix[~(i + j)][i] = \
                    matrix[~(i + j)][i], matrix[i][i + j], matrix[i + j][~i], matrix[~i][~(i + j)]

    # Reverse first
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for i in range(n // 2):
            for j in range(n - 2*i - 1):
                matrix[i][i + j], matrix[i + j][~i], matrix[~i][~(i + j)], matrix[~(i + j)][i] = \
                    matrix[~(i + j)][i], matrix[i][i + j], matrix[i + j][~i], matrix[~i][~(i + j)]

    # Built-in function
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     matrix[:] = zip(*matrix[::-1])

# @lc code=end
