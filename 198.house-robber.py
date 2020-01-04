#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        a, b = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            res = max(a + nums[i], b)
            a, b = b, res
        return res

# @lc code=end

