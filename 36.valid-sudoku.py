#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     for i in range(9):
    #         row, col, sub = set(), set(), set()
    #         for j in range(9):
    #             sub_i = i // 3 * 3 + j // 3
    #             sub_j = i % 3 * 3 + j % 3
    #             if board[i][j] in row or board[j][i] in col or board[sub_i][sub_j] in sub:
    #                 return False
    #             else:
    #                 if board[i][j] != '.':
    #                     row.add(board[i][j])
    #                 if board[j][i] != '.':
    #                     col.add(board[j][i])
    #                 if board[sub_i][sub_j] != '.':
    #                     sub.add(board[sub_i][sub_j])
    #     return True

    def isValidSudoku(self, board):
        seen = sum(([(c, i), (j, c), (i//3, j//3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))

# @lc code=end

