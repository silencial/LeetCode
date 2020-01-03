#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros, k = 0, 5
        while k <= n:
            zeros += n // k
            k = k * 5
        return zeros

# @lc code=end

