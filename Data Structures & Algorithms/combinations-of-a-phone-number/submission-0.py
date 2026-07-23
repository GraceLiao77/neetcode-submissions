class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maplist = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        res = []
        sub = []
        if not digits: return res
        def dfs(i):
            # stop base case
            if i == len(digits):
                res.append(''.join(sub))
                return
            for j in maplist[int(digits[i])]: # 'def'
                sub.append(j)
                dfs(i+1)
                sub.pop()
        dfs(0)
        return res