#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     dic = {}
    #     threshold = len(nums) // 2
    #     for i in nums:
    #         if i in dic:
    #             dic[i] += 1
    #         else:
    #             dic[i] = 1
    #         if dic[i] > threshold:
    #             return i

    # def majorityElement(self, nums: List[int]) -> int:
    #     count = 0
    #     for i in nums:
    #         if count == 0:
    #             ele = i
    #         count += 1 if ele == i else -1
    #     return ele

    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
# @lc code=end

