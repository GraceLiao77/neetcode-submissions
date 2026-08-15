class Solution:
    def numDecodings(self, s: str) -> int:
        # dfs
        # 1012 -> 10 1 2, 10 12
        cache = {}
        def dfs(i):
            if i == len(s):
                return 1 # 前面的切割完全合法 所以是一种解法
            if s[i] == '0':
                return 0 # 走不通不合法
            if i in cache:
                return cache[i] #走缓存
            way = 0
            # 切割一个
            way += dfs(i+1)
            if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                way += dfs(i+2)
            cache[i] = way
            return way
            
        # 从字符串0开始有多少种解码方式
        return dfs(0)