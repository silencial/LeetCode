#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        k = ord('A') - 1
        n = 0
        for i, c in enumerate(s[::-1]):
            n += (ord(c) - k) * 26 ** i
        return n

# @lc code=end

