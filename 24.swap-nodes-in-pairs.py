#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        a, b = head, head.next
        if not b:
            return a
        c = b.next
        a.next = self.swapPairs(c)
        b.next = a
        return b

# @lc code=end

