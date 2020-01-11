#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x, n = 1 / x, -n

        res = 1
        while n > 0:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1
    #     if x == 0:
    #         return 0
    #     if n < 0:
    #         return 1 / self.myPow(x, -n)
    #     if n % 2:
    #         return x * self.myPow(x, n - 1)
    #     return self.myPow(x * x, n // 2)

# @lc code=end
