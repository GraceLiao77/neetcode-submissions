# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.isSametree(root, subRoot):
            return True
        else:
            lres = self.isSubtree(root.left, subRoot)
            rres = self.isSubtree(root.right, subRoot)
        return lres or rres

    def isSametree(self, p, q) -> bool:
        list1 = deque([p])
        list2 = deque([q])
        while list1 and list2:
            l1 = list1.popleft()
            l2 = list2.popleft()
            if not l1 and not l2:
                continue
            if not l1 or not l2 or l1.val!= l2.val:
                return False
            list1.append(l1.left)
            list1.append(l1.right)
            list2.append(l2.left)
            list2.append(l2.right)
        return True