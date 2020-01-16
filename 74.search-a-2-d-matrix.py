#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        row_i, row_j = 0, len(matrix) - 1
        while row_i <= row_j:
            mid = (row_i + row_j) // 2
            if target < matrix[mid][0]:
                row_j = mid - 1
            elif target > matrix[mid][0]:
                row_i = mid + 1
            else:
                return True

        if target > matrix[row_j][-1]:
            return False

        col_i, col_j = 0, len(matrix[0]) - 1
        while col_i <= col_j:
            mid = (col_i + col_j) // 2
            if target < matrix[row_j][mid]:
                col_j = mid - 1
            elif target > matrix[row_j][mid]:
                col_i = mid + 1
            else:
                return True
        return False

# @lc code=end
