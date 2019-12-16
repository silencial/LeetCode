#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        node = [root]
        while node:
            res.append([])
            temp = []
            for i in node:
                if i.left:
                    temp.append(i.left)
                    res[-1].append(i.left.val)
                if i.right:
                    temp.append(i.right)
                    res[-1].append(i.right.val)
            node = temp
        return res[-2::-1]

        # Concise code
        # res, queue = [], [root]
        # while queue:
        #     res.append([node.val for node in queue if node])
        #     queue = [child for node in queue if node for child in (node.left, node.right)]
        # return res[::-1]
# @lc code=end

