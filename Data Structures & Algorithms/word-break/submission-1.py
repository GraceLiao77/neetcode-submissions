class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False] * (l+1)
        dp[0] = True

        for i in range(1, l+1):
            for w in wordDict:
                wl = len(w)
                if s[i-wl:i] == w and dp[i-wl]:
                    dp[i] = True
                    break #只要有一个单词可以那么就可以去检测下一个位置
        print(dp)
        return dp[-1]

