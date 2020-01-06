#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = set()
    #     used = set()
    #     for i, num in enumerate(nums):
    #         if num in used:
    #             continue
    #         used.add(num)
    #         x = self.twoSum(nums, i, -num)
    #         for num1, num2 in x:
    #             res.add(tuple(sorted([num, num1, num2])))
    #     return res

    # def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
    #     dic = {}
    #     res = []
    #     for i in range(start + 1, len(nums)):
    #         num = nums[i]
    #         if num in dic:
    #             res.append([num, nums[dic[num]]])
    #         else:
    #             dic[target - num] = i
    #     return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        prev_high = len(nums) - 1
        for i in range(len(nums) - 2):
            num = nums[i]
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            low, high = i + 1, prev_high
            while high > i + 1 and nums[high] > -(num + nums[low]):
                high -= 1
            prev_high = high
            while low < high:
                total = num + nums[low] + nums[high]
                if total < 0:
                    low += 1
                elif total > 0:
                    high -= 1
                else:
                    res.append([num, nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
        return res

# @lc code=end

