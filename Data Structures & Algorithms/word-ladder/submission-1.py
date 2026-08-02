class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # word -> pattern
        patternList = defaultdict(list)
        for item in wordList:
            for i in range(len(item)):
                key = item[:i] + '*' + item[i+1:]
                patternList[key].append(item)
        # *at [bat]
        # b*t [bat]
        # ba* [bat, bag]
        # *ag [bag, sag, dag]
        # b*g [bag]
        # s*g [sag]
        # sa* [sag]
        # d*g [dag]
        # da* [dag]
        # *ot [dot]
        # d*t [dot]
        # do* [dot]
        q = deque([beginWord]) #[bag]
        visited = set([beginWord])
        step = 1
        while q:
            print(q, patternList)
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return step
                for i in range(len(cur)):
                    key = cur[:i] + '*' + cur[i+1:]
                    for c in patternList[key]:
                        if c not in visited:
                            print(key)
                            q.append(c)
                            visited.add(c)
            step += 1
        return 0

