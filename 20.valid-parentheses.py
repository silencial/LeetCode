#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left = set(['(', '{', '['])
        right = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            elif stack and stack[-1] == right[i]:
                stack.pop()
            else:
                return False
        return stack == []
# @lc code=end

