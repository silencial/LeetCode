#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits[:]
        i = len(res) - 1
        while res[i] == 9:
            res[i] = 0
            i -= 1

            if i == -1:
                return [1] + res
        res[i] += 1
        return res



# @lc code=end

