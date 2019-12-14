#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if not last.startswith(first[:i + 1]):
                return first[:i]
        return first


# @lc code=end

