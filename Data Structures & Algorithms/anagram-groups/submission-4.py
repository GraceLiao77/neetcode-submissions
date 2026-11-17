class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict({})

        for s in strs:
            curkey = [0] * 26
            for i in s:
                curkey[ord(i)-ord('a')] += 1
            curkey = tuple(curkey)
            if curkey in result:
                result[curkey].append(s)
            else:
                result[curkey] = [s]
        return list(result.values())