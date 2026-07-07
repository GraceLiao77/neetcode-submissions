# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def vaild(node, low, high):
            if not node: return True
            if low >= node.val or node.val >= high:
                return False
            return vaild(node.left, low, node.val) and vaild(node.right, node.val, high)
        return vaild(root, float('-infinity'), float('infinity'))