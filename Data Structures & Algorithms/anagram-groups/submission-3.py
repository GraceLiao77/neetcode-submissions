class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maplist = defaultdict(list)
        for item in strs:
            count = [0] * 26
            for c in item:
                count[ord(c) - ord('a')] += 1
            maplist[tuple(count)].append(item) # 因为 dict/set 需要"不可变"的 key
        return list(maplist.values())
