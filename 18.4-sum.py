#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    # Similar to 3Sum
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     if len(nums) < 4:
    #         return []
    #     nums.sort()
    #     res = []
    #     if sum(nums[:4]) > target or sum(nums[-4:]) < target:
    #         return res
    #     M, pre_r = nums[-1], len(nums) - 1
    #     for i in range(0, len(nums) - 3):
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         a = nums[i]
    #         if 4 * a > target:
    #             break
    #         if a + 3 * M < target:
    #             continue
    #         # print(target, nums[i], nums[i + 1], nums[i + 2], nums[pre_r])
    #         while pre_r > i + 2 and nums[pre_r] > target - nums[i] - nums[i + 1] - nums[i + 2]:
    #             pre_r -= 1
    #         if pre_r == i + 2:
    #             break
    #         M = nums[pre_r]
    #         a_target = target - a
    #         for j in range(i + 1, len(nums) - 2):
    #             if j > i + 1 and nums[j] == nums[j - 1]:
    #                 continue
    #             b = nums[j]
    #             if 3 * b > a_target:
    #                 break
    #             if b + 2 * M < a_target:
    #                 continue
    #             l, r = j + 1, pre_r
    #             b_target = a_target - b
    #             # print('index', i, j, l, r)
    #             while l < r:
    #                 c = nums[l]
    #                 if 2 * c > b_target:
    #                     break
    #                 d = nums[r]
    #                 c_target = b_target - c
    #                 if d < c_target:
    #                     while l < r and nums[l] == nums[l + 1]:
    #                         l += 1
    #                     l += 1
    #                 elif d > c_target:
    #                     while l < r and nums[r] == nums[r - 1]:
    #                         r -= 1
    #                     r -= 1
    #                 else:
    #                     res.append([a, b, c, d])
    #                     while l < r and nums[l] == nums[l + 1]:
    #                         l += 1
    #                     while l < r and nums[r] == nums[r - 1]:
    #                         r -= 1
    #                     l += 1
    #                     r -= 1
    #     return res

    # Dict + Set
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     if not nums:
    #         return []
    #     nums.sort()
    #     L, N, S, M = len(nums), {j: i for i, j in enumerate(nums)}, set(), nums[-1]
    #     for i in range(L - 3):
    #         a = nums[i]
    #         if a + 3 * M < target:
    #             continue
    #         if 4 * a > target:
    #             break
    #         for j in range(i + 1, L - 2):
    #             b = nums[j]
    #             if a + b + 2 * M < target:
    #                 continue
    #             if a + 3 * b > target:
    #                 break
    #             for k in range(j + 1, L - 1):
    #                 c = nums[k]
    #                 d = target - (a + b + c)
    #                 if d > M:
    #                     continue
    #                 if d < c:
    #                     break
    #                 if d in N and N[d] > k:
    #                     S.add((a, b, c, d))
    #     return S

    # Generalize to NSum using recursion
    def fourSum(self, nums, target):
        def findNsum(l, r, target, N, result, results):
            if r - l + 1 < N or N < 2 or nums[l] * N > target or nums[r] * N < target:  # early termination
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
                return
            # recursively reduce N
            for i in range(l, r + 1):
                if i == l or (i > l and nums[i - 1] != nums[i]):
                    findNsum(i + 1, r, target - nums[i], N - 1, result + [nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums) - 1, target, 4, [], results)
        return results

# @lc code=end

