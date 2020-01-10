#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    # Backtracking
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     def backtracking(nums: List[int], curr: List[int]) -> None:
    #         if len(nums) == 0:
    #             res.append(curr)
    #         for i in range(len(nums)):
    #             backtracking(nums[0:i] + nums[i+1:], curr + [nums[i]])

    #     res = []
    #     backtracking(nums, [])
    #     return res

    # Iteration
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            temp = []
            for curr in res:
                for k in range(len(curr) + 1):
                    temp.append(curr[:k] + [n] + curr[k:])
            res = temp
        return res

    # One line code
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     return [[n] + p
    #             for i, n in enumerate(nums)
    #             for p in self.permute(nums[:i] + nums[i+1:])] or [[]]

    # Built-in function
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     return list(itertools.permutations(nums))

# @lc code=end

