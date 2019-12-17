#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        node = [root]
        depth = 0
        while node:
            temp = []
            depth += 1
            for i in node:
                if not (i.left or i.right):
                    return depth
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            node = temp

# @lc code=end

