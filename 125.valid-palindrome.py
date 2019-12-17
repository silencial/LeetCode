#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ''
        for i in s:
            if i.isalnum():
                res += i
        return res == res[::-1]
# @lc code=end

