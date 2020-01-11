#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > res:
                res = 0
            else:
                res += 1
        return res == 0

# @lc code=end
