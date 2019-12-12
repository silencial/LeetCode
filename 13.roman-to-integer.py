#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
        n = 0
        # s = s[::-1]
        # for i, char in enumerate(s):
        #     if i == 0:
        #         n = dic[char]
        #     else:
        #         if dic[s[i - 1]] > dic[char]:
        #             n -= dic[char]
        #         else:
        #             n += dic[char]
        # return n
        end = len(s) - 1
        for i, char in enumerate(s):
            if i == end:
                return n + dic[char]
            else:
                if dic[s[i + 1]] > dic[char]:
                    n -= dic[char]
                else:
                    n += dic[char]
# @lc code=end

