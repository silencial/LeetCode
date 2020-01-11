#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [[intervals[0][0]] * 2]
        for l in intervals:
            if l[1] > res[-1][1]:
                if l[0] <= res[-1][1]:
                    res[-1][1] = l[1]
                else:
                    res.append(l)
        return res
# @lc code=end
