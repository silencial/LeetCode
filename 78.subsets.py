#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [i + [num] for i in res]
        return res

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     n_bit = 1 << n
    #     res = []
    #     for i in range(n_bit):
    #         bit = bin(i | n_bit)[3:]

    #         res.append([nums[i] for i in range(n) if bit[i] == '1'])
    #     return res

# @lc code=end
