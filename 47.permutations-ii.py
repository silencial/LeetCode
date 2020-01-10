#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    # Backtracking
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     def backtracking(nums: List[int], curr: List[int]) -> None:
    #         if len(nums) == 0:
    #             res.append(curr)
    #         for i in range(len(nums)):
    #             if i > 0 and nums[i] == nums[i-1]:
    #                 continue
    #             backtracking(nums[:i] + nums[i+1:], curr + [nums[i]])

    #     nums.sort()
    #     res = []
    #     backtracking(nums, [])
    #     return res

    # Iterative
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            temp = []
            for curr in res:
                for i in range(len(curr) + 1):
                    temp.append(curr[:i] + [n] + curr[i:])
                    if i < len(curr) and curr[i] == n:
                        break
            res = temp
        return res

# @lc code=end
