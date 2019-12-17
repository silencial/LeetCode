#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        val = sum - root.val
        if root.left is None and root.right is None and val == 0:
            return True
        if root.left and root.right:
            return self.hasPathSum(root.left, val) or self.hasPathSum(root.right, val)
        elif root.left:
            return self.hasPathSum(root.left, val)
        else:
            return self.hasPathSum(root.right, val)

    # Concise code
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     if not root:
    #         return False
    #     val = sum - root.val
    #     if root.left is None and root.right is None and val == 0:
    #         return True
    #     return self.hasPathSum(root.left, val) or self.hasPathSum(root.right, val)
# @lc code=end

