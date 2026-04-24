class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # charCount: [str1, str2...]
        for i in strs:
            count = [0] * 26 #a-z
            for s in i:
                count[ord(s) - ord('a')] += 1;
            res[tuple(count)].append(i)

        return list(res.values())



