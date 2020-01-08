#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        newhead = ListNode(0)
        newhead.next = head
        first = second = newhead
        for i in range(n + 1):
            second = second.next
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return newhead.next

# @lc code=end

