#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(numRows - 1):
            prev = res[-1]
            curr = [0] + prev
            for j in range(len(prev)):
                curr[j] += prev[j]
            res.append(curr)
        return res
# @lc code=end

