class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for item in word:
            if item not in cur.children:
                cur.children[item] = TreeNode()
            cur = cur.children[item]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd     # ← 走完了才检查

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True     # ← 走完了就是 True，不看 isEnd
        
        