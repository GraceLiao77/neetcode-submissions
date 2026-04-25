class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int) # {1: 1, 2: 4, 3: 3}
        for i in nums:
            res[i] += 1
            
        ressort = sorted(res, key=res.get, reverse=True)
        return ressort[:k]
            

        