class Solution:
    def numDecodings(self, s: str) -> int:
        # DP
        dp = [0] * (len(s)+1)
        dp[len(s)] = 1
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                dp[i] = 0
                continue
            # 吃一个
            dp[i] += dp[i+1]
            #  吃两个
            if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
        return dp[0]
        # # dfs
        # # 1012 -> 10 1 2, 10 12
        # cache = {}
        # def dfs(i):
        #     if i == len(s):
        #         return 1 # 前面的切割完全合法 所以是一种解法
        #     if s[i] == '0':
        #         return 0 # 走不通不合法
        #     if i in cache:
        #         return cache[i] #走缓存
        #     way = 0
        #     # 切割一个 第一次切1 dfs(1)-> 下一个要处理剩余的'012'这些字符
        #     way += dfs(i+1)
        #     if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
        #         way += dfs(i+2)
        #     # 最终统计总数，一次吃掉一个和一次吃掉两个是不同的处理方案
        #     cache[i] = way
        #     return way
            
        # # 从字符串0开始有多少种解码方式
        # return dfs(0)