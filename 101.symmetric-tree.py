#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursion
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.symmetric(root.left, root.right)
    def symmetric(self, p: TreeNode, q: TreeNode) -> bool:
        if bool(p) != bool(q):
            return False
        if not (p or q):
            return True
        if p.val != q.val:
            return False
        return self.symmetric(p.left, q.right) and self.symmetric(p.right, q.left)

    # Iteration
    # from collections import deque
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if root is None:
    #         return True
    #     deq = deque([(root.left, root.right)])
    #     while deq:
    #         p, q = deq.popleft()
    #         if not self.check(p, q):
    #             return False
    #         if p:
    #             deq.append((p.left, q.right))
    #             deq.append((p.right, q.left))
    #     return True

    # def check(self, p: TreeNode, q: TreeNode) -> bool:
    #     return p.val == q.val if p and q else p == q

# @lc code=end

