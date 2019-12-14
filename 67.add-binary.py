#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # if len(b) > len(a):
        #     a, b = b, a
        # n = len(a)
        # pre = 0
        # for i in b[::-1]:
        #     n -= 1
        #     digit = int(a[n])
        #     digit = digit + int(i) + pre
        #     if digit > 1:
        #         digit -= 2
        #         pre = 1
        #     else:
        #         pre = 0
        #     a = a[:n] + str(digit) + a[n + 1:]
        # if pre > 0 and n > 0:
        #     pos = a[:n].rfind('0')
        #     if pos > 0:
        #         a = a[:pos] + '1' + '0' * (n - 1 - pos) + a[n:]
        #     else:
        #         a = '1' + '0' * n + a[n:]
        # elif pre > 0:
        #     a = '1' + a

        # return a

        # Cheating
        return bin(int(a, base=2) + int(b, base=2))[2:]
# @lc code=end

