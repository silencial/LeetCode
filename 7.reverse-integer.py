#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INTMAX = 2 ** 31 - 1
        rev = 0
        while x != 0:
            pop = x % 10
            x = x // 10
            if x < 0 and pop != 0:
                pop -= 10
                x += 1
            if rev > int(INTMAX / 10) or rev == INTMAX and pop > 7:
                return 0
            if rev < int(-INTMAX / 10) or rev == -INTMAX and pop < -8:
                return 0
            rev = rev * 10 + pop
        return rev


# @lc code=end

