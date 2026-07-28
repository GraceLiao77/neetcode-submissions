"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}

        def dfs(n):
            # if it's already existing
            if n in oldToNew:
                return oldToNew[n]
            # else create a new, first store to hashmap
            new = Node(n.val)
            oldToNew[n] = new
            # recrusive nei
            for i in n.neighbors:
                new.neighbors.append(dfs(i))
            
            return new
        return dfs(node)


