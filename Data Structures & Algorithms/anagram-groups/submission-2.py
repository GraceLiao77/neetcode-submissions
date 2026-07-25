class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maplist = defaultdict(list)
        for item in strs:
            count = [0] * 26
            for c in item:
                count[ord(c) - ord('a')] += 1
            maplist[tuple(count)].append(item)
        return list(maplist.values())
