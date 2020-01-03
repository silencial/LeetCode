#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    # def reverseBits(self, n: int) -> int:
    #     r = bin(n)[:1:-1]
    #     return int(r + '0' * (32 - len(r)), 2)

    # def reverseBits(self, n: int) -> int:
    #     bit = res = 0
    #     while n % 2 == 0 and n > 0:
    #         n /= 2
    #         bit += 1
    #     while n > 0:
    #         res *= 2
    #         res += n % 2
    #         n //= 2
    #         bit += 1
    #     return int(res * 2 ** (32 - bit))

    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res

# @lc code=end

