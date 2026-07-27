class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(n, node):
            if n == len(word):
                return node.isEnd
            if word[n] == '.':
                for i in node.children:
                    if dfs(n+1, node.children[i]):
                        return True
                return False
            else:
                if word[n] not in node.children:
                    return False
                else:
                    if dfs(n+1, node.children[word[n]]):
                        return True
                return False
        return dfs(0, cur)
