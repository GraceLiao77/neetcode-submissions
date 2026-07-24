class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = defaultdict(int)
        for i in s:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
        
        for j in t:
            if j in res:
                res[j] -= 1
                if res[j] == 0:
                    del res[j]
            else:
                return False
        if not res:
            return True
        return False

