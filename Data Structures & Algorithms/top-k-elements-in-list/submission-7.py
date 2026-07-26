# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         res = defaultdict(int) # {1: 1, 2: 4, 3: 3}
#         for i in nums:
#             res[i] += 1   #O(n)
#         ressort = sorted(res, key=res.get, reverse=True) # nlogn
#         return ressort[:k]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nmap = {}
        for i in nums:
            nmap[i] = 1 + nmap.get(i, 0)
        
        bucket = [[] for _ in range(len(nums)+1)]

        for key, val in nmap.items():
            bucket[val].append(key)
        print(bucket)
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                if len(res) < k:
                    res.append(n)
        return res

            


            

        