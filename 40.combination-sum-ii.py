#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtracking(i + 1, prev + [candidates[i]], residual - candidates[i])

        backtracking(0, [], target)
        return res
# @lc code=end

