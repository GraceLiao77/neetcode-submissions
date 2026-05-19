class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1len = len(s1)
        r = s1len
        s1map = defaultdict(int)
        for i in s1:
            s1map[i] += 1
        curmap = defaultdict(int)
        for j in s2[l:r]:
            curmap[j] += 1
        while r <= len(s2):
            print(curmap,s1map )
            if curmap == s1map:
                return True
            curmap[s2[l]] -= 1
            if curmap[s2[l]] == 0:
                del curmap[s2[l]]
            l += 1
            r = l + s1len - 1
            if r >= len(s2):
                return False
            curmap[s2[r]] += 1
        return False

        


        
            



        