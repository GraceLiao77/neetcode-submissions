class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, piles[-1]
        min_k = float('inf')
        while l <= r:
            total_h = 0
            k = (l + r) // 2
            for i in piles:
                if i < k:
                    total_h += 1
                else:
                    if i % k == 0:
                        total_h += i // k
                    else:
                        total_h += ((i // k) + 1)
            if total_h <= h:
                min_k = min(min_k, k)
                r = k - 1
            elif total_h > h:
                l = k + 1
        return min_k