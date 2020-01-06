#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        pre_r = len(nums) - 1
        for i in range(0, len(nums) - 3):
            if nums[i] > target and nums[i] > 0:
                break
            if nums[-1] < target and nums[-1] < 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # print(target, nums[i], nums[i + 1], nums[i + 2], nums[pre_r])
            while pre_r > i + 2 and nums[pre_r] > target - nums[i] - nums[i + 1] - nums[i + 2]:
                pre_r -= 1
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, pre_r
                # print('index', i, j, l, r)
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total < target:
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                    elif total > target:
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res

# @lc code=end

