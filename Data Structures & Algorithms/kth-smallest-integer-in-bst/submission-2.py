# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while stack or cur:
            # left first
            while cur:
                stack.append(cur)
                cur = cur.left
            res = stack.pop()
            k -= 1
            if k == 0:
                return res.val
            cur = res.right
            

        # res = root.val
        # count = k
        # def dfs(node):
        #     nonlocal count, res
        #     if not node:
        #         return
        #     dfs(node.left)
        #     if count == 0:
        #         return
        #     count -= 1
        #     if count == 0:
        #         res = node.val
        #         return
        #     dfs(node.right)
        # dfs(root)
        # print(res)
        # return res