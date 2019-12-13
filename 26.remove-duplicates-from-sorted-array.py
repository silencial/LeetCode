#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1

        i = 0
        for j in nums:
            if j != nums[i]:
                i += 1
                nums[i] = j
        return i + 1


# @lc code=end

