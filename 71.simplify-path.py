#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    # def simplifyPath(self, path: str) -> str:
    #     i, n = 0, len(path)
    #     res = []
    #     while i < n:
    #         while i < n and path[i] == '/':
    #             i += 1
    #         j = i
    #         while j < n and path[j] != '/':
    #             j += 1
    #         s = path[i:j]
    #         # print(i, j, s)
    #         if s == '..':
    #             if res:
    #                 res.pop()
    #         elif s and s != '.':
    #             res.append(s)
    #         i = j + 1
    #     return '/' + '/'.join(res)

    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        res = []
        for s in path:
            if s == '' or s == '.':
                continue
            if s == '..':
                if res:
                    res.pop()
            else:
                res.append(s)
        return '/' + '/'.join(res)

# @lc code=end
