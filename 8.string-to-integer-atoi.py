#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if not str:
            return 0
        t = str[0]
        if t != '+' and t != '-' and not t.isdigit():
            return 0
        INTMAX = 2 ** 31 - 1
        q, r = divmod(INTMAX, 10)
        if t.isdigit():
            pos = True
        else:
            pos = True if t == '+' else False
            str = str[1:]

        n = 0
        for i in str:
            if not i.isdigit():
                break
            if n > q:
                return INTMAX if pos else -INTMAX - 1
            if n == q:
                if pos and int(i) >= r:
                    return INTMAX
                if not pos and int(i) > r:
                    return -INTMAX - 1
            n = n * 10 + int(i)
        return n if pos else -n

# @lc code=end

