#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    # Recursion
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k or k < 1:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        pre1 = self.combine(n - 1, k - 1)
        for l in pre1:
            l.append(n)
        return pre1 + self.combine(n - 1, k)

    # Iterative
    # def combine(self, n, k):
    #     res = []
    #     stack = []
    #     x = 1
    #     while True:
    #         l = len(stack)
    #         if l == k:
    #             res.append(stack[:])
    #         if l == k or x > n - k + l + 1:
    #             if not stack:
    #                 return res
    #             x = stack.pop() + 1
    #         else:
    #             stack.append(x)
    #             x += 1

# @lc code=end
