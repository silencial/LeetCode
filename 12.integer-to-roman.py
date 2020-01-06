#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    # def intToRoman(self, num: int) -> str:
    #     n, s = 1000, ''
    #     one = ['I', 'X', 'C', 'M']
    #     five = ['V', 'L', 'D']
    #     for i in range(3, -1, -1):
    #         q, num = divmod(num, n)
    #         n //= 10
    #         if q == 0:
    #             continue
    #         if q > 0 and q < 4:
    #             s += q * one[i]
    #         elif q == 4:
    #             s += one[i] + five[i]
    #         elif q == 5:
    #             s += five[i]
    #         elif q > 5 and q < 9:
    #             s += five[i] + (q - 5) * one[i]
    #         elif q == 9:
    #             s += one[i] + one[i + 1]
    #     return s

    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res, i = '', 0
        while num:
            res += (num // values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return res

# @lc code=end

