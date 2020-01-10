#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    # Sorted array as key in dict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return res.values()

    # Use 26 char as keys
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     import collections
    #     k = ord('a')
    #     res = collections.defaultdict(list)
    #     for s in strs:
    #         key = [0] * 26
    #         for t in s:
    #             key[ord(t) - k] += 1
    #         # print(key)
    #         res[tuple(key)].append(s)
    #     return re

    # Prime number property
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     primes = {'a': 2, 'b': 3, 'c': 5,
    #               'd': 7, 'e': 11, 'f': 13,
    #               'g': 17, 'h': 19, 'i': 23,
    #               'j': 29, 'k': 31, 'l': 37,
    #               'm': 41, 'n': 43, 'o': 47,
    #               'p': 53, 'q': 59, 'r': 61,
    #               's': 67, 't': 71, 'u': 73,
    #               'v': 79, 'w': 83, 'x': 89,
    #               'y': 97, 'z': 101
    #               }

    #     res = {}
    #     for string in strs:
    #         product = 1
    #         for character in string:
    #             product = primes[character] * product
    #         if product in res:
    #             res[product].append(string)
    #         else:
    #             res[product] = [string]

    #     return res.values()

# @lc code=end
