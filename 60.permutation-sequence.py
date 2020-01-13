#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [i for i in range(1, n + 1)]
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i

        res = ''
        k -= 1
        for i in range(n - 1, -1, -1):
            index, k = divmod(k, factorial[i])
            res += str(numbers[index])
            del numbers[index]

        return res

# @lc code=end
