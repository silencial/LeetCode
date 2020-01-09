#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     n = len(candidates)
    #     res = []
    #     def backtracking(start: int, prev: List[int], residual: int) -> None:
    #         if residual < 0:
    #             return
    #         if residual == 0:
    #             res.append(prev)
    #             return
    #         for i in range(start, n):
    #             backtracking(i, prev + [candidates[i]], residual - candidates[i])

    #     backtracking(0, [], target)
    #     return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()
        def backtracking(start: int, prev: List[int], residual: int) -> None:
            if residual < 0:
                return
            if residual == 0:
                res.append(prev)
                return
            for i in range(start, n):
                if candidates[i] > residual:
                    break
                backtracking(i, prev + [candidates[i]], residual - candidates[i])

        backtracking(0, [], target)
        return res

# @lc code=end

