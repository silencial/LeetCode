#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        col = ''
        k = ord('A')
        while n > 0:
            n, r = divmod(n - 1, 26)
            col = chr(r + k) + col
        return col

# @lc code=end

