# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         res = defaultdict(int) # {1: 1, 2: 4, 3: 3}
#         for i in nums:
#             res[i] += 1   #O(n)
#         ressort = sorted(res, key=res.get, reverse=True) # nlogn
#         return ressort[:k]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]#[[], []]
        count = defaultdict(int) # {1: 2, 2: 3, 3: 5}
        for n in nums:
            count[n] += 1 # {1: 2, 2: 3, 3: 5}
        for key, val in count.items():
            bucket[val].append(key)
        # defaultdict(<class 'int'>, {1: 1, 2: 2, 3: 3}) [[1], [2], [3], [], [], [], []]
        print(bucket)
        sequence = []
        for m in range(len(bucket)-1, 0, -1):
            sequence.extend(bucket[m])
            if len(sequence) >= k:
                return sequence


            

        