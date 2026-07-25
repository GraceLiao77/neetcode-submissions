class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    def addWords(self, word) -> TrieNode:
        cur = self # root.addWord("cat") self = root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode() ####
            cur = cur.children[i]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # all words add to the trie tree
        root = TrieNode()
        for item in words:
            root.addWords(item)
        
        row, col = len(board),len(board[0])
        res = []

        def dfs(r, c, node):
            # 出界
            if not node:
                return
            # 检查是否合法
            if (r < 0 or r >= row or c < 0 or c >= col or
                board[r][c] == '#' or board[r][c] not in node.children):
                return
            # 合法：走一步判断这个字符串是不是最后一个
            ch = board[r][c]
            nextNode = node.children[ch] 
            # 判断是不是符合要求的word
            if nextNode.word:
                res.append(nextNode.word)
                nextNode.word = None
            # choice
            board[r][c] = '#'
            
            # dfs
            dfs(r-1, c, nextNode)
            dfs(r+1, c, nextNode)
            dfs(r, c-1, nextNode)
            dfs(r, c+1, nextNode)

            # undo
            board[r][c] = ch
            

        for r in range(row):
            for c in range(col):
                dfs(r, c, root)
        
        return res
        