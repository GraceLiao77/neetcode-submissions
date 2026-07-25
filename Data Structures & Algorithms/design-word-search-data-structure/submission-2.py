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
        def dfs(node, i):
            cur = node
            if i == len(word):
                return cur.isEnd
            if word[i] != '.':
                if word[i] in cur.children:
                    return dfs(cur.children[word[i]], i+1)
                else:
                    return False
            else:
                for k in cur.children:
                    if dfs(cur.children[k], i+1):
                        return True
                return False

        return dfs(self.root, 0)

        
                




        
