#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        i = j = 0
        n = len(nums)
        while j < n:
            if nums[j] == val:
                nums[j] = nums[n - 1]
                n -= 1
            else:
                j += 1
        return n
# @lc code=end

