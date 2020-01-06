#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] > target and nums[0] > 0:
            return sum(nums[0:3])
        if nums[-1] < target and nums[-1] < 0:
            return sum(nums[-3:])
        dmin, res = 999, 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                # print(i, l, r, total, target, dmin, res)
                if abs(total - target) < dmin:
                    dmin = abs(total - target)
                    res = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target
        return res

# @lc code=end

