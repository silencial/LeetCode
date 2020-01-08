#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INTMIN = -1 << 31
        if dividend == INTMIN and divisor == -1:
            return - (INTMIN + 1)
        if divisor == INTMIN:
            if dividend == INTMIN:
                return 1
            else:
                return 0
        b = abs(divisor)
        if dividend < 0:
            a = dividend + b
            if a > 0:
                return 0
        else:
            a = dividend - b
            if a < 0:
                return 0
        a = abs(a)
        q = 0
        for i in range(31, -2, -1):
            if a < b:
                return q + 1 if (dividend > 0) == (divisor > 0) else -q - 1
            if a >> i >= b:
                q += 1 << i
                a -= b << i
# @lc code=end

