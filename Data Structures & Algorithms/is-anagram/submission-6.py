class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        res = [0] * 26
        for i in range(len(s)):
            # ord('b')-ord('a') = 1
            # ord('c')-ord('a') = 2
            # ord('d')-ord('a') = 3
            res[ord(s[i]) - ord('a')] += 1
            res[ord(t[i]) - ord('a')] -= 1
        
        for j in res:
            if j != 0:
                return False
        return True
            


        # res = defaultdict(int)
        # for i in s:
        #     if i not in res:
        #         res[i] = 1
        #     else:
        #         res[i] += 1
        
        # for j in t:
        #     if j in res:
        #         res[j] -= 1
        #         if res[j] == 0:
        #             del res[j]
        #     else:
        #         return False
        # if not res:
        #     return True
        # return False

