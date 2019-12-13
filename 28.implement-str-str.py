#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        if n > h:
            return -1
        for i in range(h - n + 1):
            if (haystack[i:i + n]) == needle:
                return i
        return -1

# @lc code=end

