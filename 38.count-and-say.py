#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        pre = self.countAndSay(n - 1)
        s = ''
        a = pre[0]
        n = 1
        for i in pre[1:]:
            if i != a:
                s += str(n) + a
                n = 1
                a = i
            else:
                n += 1
        return s + str(n) + a
# @lc code=end

