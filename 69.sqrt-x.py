#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        i1 = 1
        i2 = 3
        while abs(i1 - i2) >= 1:
            i2 = i1
            i1 = (i1 + x / i1) / 2
        return int(i1)
# @lc code=end

