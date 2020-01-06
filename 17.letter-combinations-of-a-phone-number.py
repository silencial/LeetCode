#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    # BackTracking
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits:
    #         return []
    #     phone = {'2': 'abc',
    #              '3': 'def',
    #              '4': 'ghi',
    #              '5': 'jkl',
    #              '6': 'mno',
    #              '7': 'pqrs',
    #              '8': 'tuv',
    #              '9': 'wxyz'}
    #     def addString(curr: str, digits: str) -> None:
    #         if len(digits) == 0:
    #             res.append(curr)
    #             return
    #         for i in phone[digits[0]]:
    #             addString(curr + i, digits[1:])
    #     res = []
    #     addString('', digits)
    #     return res

    # Use itertools
    # def letterCombinations(self, digits: str):
    #     if digits == "":
    #         return []
    #     phone = {'2': 'abc',
    #              '3': 'def',
    #              '4': 'ghi',
    #              '5': 'jkl',
    #              '6': 'mno',
    #              '7': 'pqrs',
    #              '8': 'tuv',
    #              '9': 'wxyz'}
    #     input = []
    #     for d in digits:
    #         input.append(phone[d])
    #     import itertools
    #     result = list(itertools.product(*input))
    #     for i in range(len(result)):
    #         string = ""
    #         for c in result[i]:
    #             string += c
    #         result[i] = string
    #     return result

    # Use reduce
    def letterCombinations(self, digits):
        if not digits:
            return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        import functools
        return functools.reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])

# @lc code=end

