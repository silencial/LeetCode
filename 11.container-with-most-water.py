#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxs, low, high = 0, 0, len(height) - 1
        while low < high:
            if height[low] < height[high]:
                maxs, low = max(maxs, height[low] * (high - low)), low + 1
            else:
                maxs, high = max(maxs, height[high] * (high - low)), high - 1
        return maxs

# @lc code=end

