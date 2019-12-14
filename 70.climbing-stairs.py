#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
import math

class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if n == 1:
            return a
        if n == 2:
            return b
        for i in range(2, n):
            a, b = b, a + b
        return b

        # a = math.sqrt(5)
        # return int(1 / a * (math.pow((1 + a) / 2, n + 1) - math.pow((1 - a) / 2, n + 1)))

# @lc code=end

