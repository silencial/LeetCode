#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    # Expand around center
    # def longestPalindrome(self, s: str) -> str:
    #     l, res = 0, ''
    #     for i in range(0, len(s)):
    #         res = max(self.palindrome(s, i, i), self.palindrome(s, i, i + 1), res, key=len)
    #     return res

    # def palindrome(self, s: str, low: int, high: int) -> str:
    #     while low > -1 and high < len(s) and s[low] == s[high]:
    #         low -= 1
    #         high += 1
    #     return s[low + 1:high]

    # Expand around center with trick
    # def longestPalindrome(self, s):
    #     lenS = len(s)
    #     if lenS <= 1:
    #         return s
    #     minStart, maxLen, i = 0, 1, 0
    #     while i < lenS:
    #         if lenS - i <= maxLen / 2:
    #             break
    #         j, k = i, i
    #         while k < lenS - 1 and s[k] == s[k + 1]:
    #             k += 1
    #         i = k + 1
    #         while k < lenS - 1 and j and s[k + 1] == s[j - 1]:
    #             k, j = k + 1, j - 1
    #         if k - j + 1 > maxLen:
    #             minStart, maxLen = j, k - j + 1
    #     return s[minStart: minStart + maxLen]

    # Manacher's Algorithm
    def longestPalindrome(self, s: str) -> str:
        T = '#' + '#'.join(s) + '#'
        C, R = 0, -1
        maxC, maxrad = 0, 1
        n = len(T)
        P = [0] * n
        for i in range(0, n):
            if n - i < maxrad:
                break
            if i < R:
                rad = min(R - i, P[2 * C - i])
            else:
                rad = 0
            while i + rad < len(T) and i - rad > -1 and T[i + rad] == T[i - rad]:
                rad += 1
            P[i] = rad
            if i + rad > R:
                C, R = i, i + rad
                if rad > maxrad:
                    maxrad, maxC = rad, i
        return s[(maxC - maxrad + 1) // 2:(maxC + maxrad) // 2]

# @lc code=end

