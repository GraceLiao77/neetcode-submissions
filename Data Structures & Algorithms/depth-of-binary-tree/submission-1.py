# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS stack
        if not root: return 0
        node = [[root, 1]]
        res = 0
        while node:
            item, depth = node.pop()
            if item:
                res = max(res, depth)
                node.append([item.left, depth + 1])
                node.append([item.right, depth + 1])
        return res

        # recursive
        # if not root: return 0

        # rightres = self.maxDepth(root.right) + 1
        # leftres = self.maxDepth(root.left) + 1

        # return max(rightres, leftres)
    