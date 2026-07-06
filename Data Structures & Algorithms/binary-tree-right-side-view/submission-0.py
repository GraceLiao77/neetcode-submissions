# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q = deque()
        q.append([1, root])
        res.append(root.val)
        while q:
            for i in range(len(q)):
                l, n = q.popleft()
                if n.right:
                    q.append([l + 1, n.right])
                if n.left:
                    q.append([l + 1, n.left])
            print(l+1, q, len(res))
            if len(res) < l+1 and q:
                le, no = q[0]
                res.append(no.val)
        return res


                