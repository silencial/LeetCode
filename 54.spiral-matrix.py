#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    # Recursion
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def helper(i: int, res) -> None:
            if 2 * i == s:
                return
            if 2 * i == s - 1:
                if n >= m:
                    res += matrix[i][i:n - i]
                else:
                    res += [vec[i] for vec in matrix[i:m - i]]
                return

            res += matrix[i][i:-i - 1] + [vec[-i - 1] for vec in matrix[i:-i - 1]] \
                + matrix[-i - 1][-i - 1:i:-1] + [vec[i] for vec in matrix[-i - 1:i:-1]]
            helper(i + 1, res)

        res = []
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])
        s = min(m, n)
        helper(0, res)
        return res

    # Loop
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     if not matrix:
    #         return []
    #     top = left = 0
    #     bot, right = len(matrix), len(matrix[0])
    #     res = []
    #     while top < bot and left < right:
    #         res += matrix[top][left:right]
    #         top += 1
    #         res += [vec[right - 1] for vec in matrix[top:bot]]
    #         right -= 1
    #         if top < bot:
    #             res += matrix[bot - 1][left:right][::-1]
    #             bot -= 1
    #         if left < right:
    #             res += [vec[left] for vec in matrix[top:bot]][::-1]
    #             left += 1
    #     return res

# @lc code=end
