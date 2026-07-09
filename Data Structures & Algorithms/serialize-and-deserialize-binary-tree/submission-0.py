# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return 'N'
            left = dfs(node.left)
            right = dfs(node.right)
            return str(node.val) + ',' + str(left) + ',' + str(right)
        return dfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        newdata = data.split(',')
        self.idx = 0
        def dedfs():
            if newdata[self.idx] == 'N':
                self.idx += 1
                return None
            node = TreeNode(newdata[self.idx])
            self.idx += 1
            node.left = dedfs()
            node.right = dedfs()
            return node
            
        return dedfs()
