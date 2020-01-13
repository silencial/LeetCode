#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        c, n = head, 0
        while c:
            c = c.next
            n += 1
        k %= n
        if k == 0:
            return head

        a = b = head
        for i in range(k):
            b = b.next
        while b.next:
            a = a.next
            b = b.next
        res = a.next
        b.next = head
        a.next = None
        return res

# @lc code=end
