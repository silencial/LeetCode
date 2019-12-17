#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 99999
        profit = 0
        for i in prices:
            if i < low:
                low = i
            else:
                profit = max(profit, i - low)
        return profit

# @lc code=end

