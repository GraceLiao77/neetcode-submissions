class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {i: [] for w in words for i in w}

        def compare(a, b):
            l1, l2 = len(a), len(b)
            i = j = 0
            while i < l1 and j < l2:
                if a[i] != b[j]:
                    adj[a[i]].append(b[j])
                    return True
                i += 1
                j += 1
            if l1 > l2:
                return False
            return True
        
        for idx in range(len(words)-1):
            if not compare(words[idx], words[idx+1]):
                return ''
        # topological sort
        indegree = {i: 0 for i in adj} #loop key
        for key in adj:
            for i in adj[key]:
                indegree[i] += 1 #有前置字母
        print(adj, indegree)
        q = deque()
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)
        visited = []
        while q:
            print('q', q)
            cur = q.popleft()
            visited.append(cur)
            for item in adj[cur]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    q.append(item)
        return ''.join(visited) if len(visited) == len(adj) else ''
