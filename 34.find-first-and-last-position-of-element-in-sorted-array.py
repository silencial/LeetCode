#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]

        left = l
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if target == nums[mid]:
                l = mid
            else:
                r = mid - 1
        return [left, r]

# @lc code=end

