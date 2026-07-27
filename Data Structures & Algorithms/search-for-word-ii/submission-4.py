class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = None
    def addwords(self, word):
        cur = self
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isword = word
   
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        # contribute TrieTree
        self.root = TrieNode()
        for i in words:
            self.root.addwords(i)
        row = len(board)
        col = len(board[0])
        # comapre between board and words tree
        def dfs(r, c, node): # row, col, rest of the tree
            # finished
            if node.isword:
                res.append(node.isword)
                node.isword = None
            # unvailded
            if (r < 0 or c < 0 or r >= row or c >= col or
                board[r][c] == '#' or
                board[r][c] not in node.children):
                return
            
            
            tmp = board[r][c] 
            board[r][c] = '#' 
            dfs(r+1, c, node.children[tmp])
            dfs(r-1, c, node.children[tmp]) 
            dfs(r, c+1, node.children[tmp]) 
            dfs(r, c-1, node.children[tmp]) 
            board[r][c] = tmp

        for r in range(row):
            for c in range(col):
                dfs(r, c, self.root)

        return res