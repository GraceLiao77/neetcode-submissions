class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        def isPali(s) -> bool:
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def dfs(i):
            # stop: when i == len(s)
            if i == len(s):
                res.append(sub[:])
                return
            # choice
            # i=0,j=i=0,sub = ['a'] dfs(1)
            # i=j=1 sub = ['a','a'] dfs(2)
            # i=j=2 sub = ['a','a','b'] -> res = [['a','a','b']] return
            # i=j=1 sub = ['a','a']
            for j in range(i, len(s)):
                if isPali(s[i:j+1]):
                    sub.append(s[i:j+1])
                    dfs(j+1)
                    # undo
                    sub.pop()

        dfs(0)
        return res

        



        