#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def addParenthesis(p: str, left: int, right: int):
            if left == n:
                res.append(p + ')' * (n - right))
                return
            addParenthesis(p + '(', left + 1, right)
            if left > right:
                addParenthesis(p + ')', left, right + 1)

        res = []
        addParenthesis('', 0, 0)
        return res

# @lc code=end

