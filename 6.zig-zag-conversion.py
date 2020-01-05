#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [""] * numRows
        down = False
        row = 0
        for i in s:
            res[row] += i
            if row == 0 or row == numRows - 1:
                down = not down
            row += 1 if down else -1
        return "".join(res)

# @lc code=end

