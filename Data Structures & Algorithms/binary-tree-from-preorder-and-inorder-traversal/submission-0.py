# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        mid = inorder.index(preorder[0])
        l_inorder = inorder[:mid]
        r_inorder = inorder[mid+1:]
        l_preorder = preorder[1:len(l_inorder)+1]
        r_preorder = preorder[len(l_inorder)+1:]
        root = TreeNode(preorder[0])
        root.left = self.buildTree(l_preorder, l_inorder)
        root.right = self.buildTree(r_preorder, r_inorder)
        return root
