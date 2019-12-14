#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ins = m + n
        while n > 0:
            ins -= 1
            if m <= 0 or nums1[m - 1] < nums2[n - 1]:
                nums1[ins] = nums2[n - 1]
                n -= 1
            else:
                nums1[ins] = nums1[m - 1]
                m -= 1

# @lc code=end

