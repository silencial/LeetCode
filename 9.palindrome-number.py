#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x1 = x
        rev = 0
        while x1 != 0:
            pop = x1 % 10
            x1 = x1 // 10
            rev = rev * 10 + pop
        if rev != x:
            return False
        return True

# @lc code=end

