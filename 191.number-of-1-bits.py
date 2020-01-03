#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     num = 0
    #     while n > 0:
    #         num += n % 2
    #         n //= 2
    #     return num

    # def hammingWeight(self, n: int) -> int:
    #     num = 0
    #     for _ in range(32):
    #         num += n & 1
    #         n >>= 1
    #     return num

    def hammingWeight(self, n: int) -> int:
        num = 0
        while n > 0:
            num += 1
            n &= n - 1
        return num

# @lc code=end

