class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        def dfs(open, close):
            # stop
            if open == n and close == n:
                res.append(''.join(subset))
                return
            # add (
            if open < n:
                subset.append('(')
                dfs(open+1, close)
                subset.pop()
            # add )
            if close < open:
                subset.append(')')
                dfs(open, close+1)
                subset.pop()

        dfs(0, 0)
        return res