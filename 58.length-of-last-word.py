#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # n = 0
        # for i in s[::-1]:
        #     if i == ' ' and n > 0:
        #         return n
        #     elif i != ' ':
        #         n += 1
        # return n

        s = s.rstrip()
        i = s.rfind(' ')
        return len(s) - i - 1

# @lc code=end

