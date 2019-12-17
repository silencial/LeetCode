#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # HashTable
    # def hasCycle(self, head: ListNode) -> bool:
    #     nodes = set()
    #     while head:
    #         if head in nodes:
    #             return True
    #         nodes.add(head)
    #         head = head.next
    #     return False

    # Slow-Fast runner
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
# @lc code=end

