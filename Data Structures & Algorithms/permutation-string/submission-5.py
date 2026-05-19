class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1len = len(s1)
        r = s1len
        while r <= len(s2):
            if self.checkstrmap(s2[l:r]) == self.checkstrmap(s1):
                return True
            l += 1
            r = l + s1len
        return False

    def checkstrmap(self, s) -> dict:
        smap = defaultdict(int)
        for i in s:
            smap[i] += 1
        return smap


        
            



        