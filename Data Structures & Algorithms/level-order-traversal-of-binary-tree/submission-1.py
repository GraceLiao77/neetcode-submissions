# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        res = []
        q = deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                curnode = q.popleft()
                if curnode:
                    level.append(curnode.val)
                    q.append(curnode.left)
                    q.append(curnode.right)
            if level:
                res.append(level)
        return res

        # dfs
        # res = []
        # def dfs(node, depth) -> List[List[int]]:
        #     if not node:
        #         return None
        #     if depth < len(res):
        #         res[depth].append(node.val)
        #     else:
        #         res.append([node.val])
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        # dfs(root, 0)
        # return res
