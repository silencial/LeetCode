#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [0] * (rowIndex + 1)
        res[0] = res[-1] = 1
        num = 1
        for i in range(1, rowIndex // 2 + 1):
            num = num * (rowIndex + 1 - i) // i
            res[i] = res[-i - 1] = num
        return res

# @lc code=end

