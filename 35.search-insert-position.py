#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
# @lc code=end

