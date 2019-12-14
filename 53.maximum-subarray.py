#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
# O(n) solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        O(n) solution
        n = maximum = nums[0]
        for i in nums[1:]:
            if n < i and n < 0:
                n = i
                maximum = max(maximum, n)
            else:
                n += i
                maximum = max(maximum, n)
        return maximum

# Divide and Conquer
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> Tuple[int, int, int, int]:
#         _, m, *_ = self.maxSub(nums)
#         return m

#     def maxSub(self, nums: List[int]) -> tuple:
#         if len(nums) == 1:
#             return nums[0], nums[0], nums[0], nums[0]
#         mid = len(nums) // 2
#         l1, m1, r1, s1 = self.maxSub(nums[:mid])
#         l2, m2, r2, s2 = self.maxSub(nums[mid:])
#         l = max(l1, s1 + l2)
#         m = max(m1, m2, r1 + l2)
#         r = max(r2, s2 + r1)
#         s = s1 + s2
#         return l, m, r, s
# @lc code=end

