class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            f = heapq.heappop(stones)
            s = heapq.heappop(stones)
            heapq.heappush(stones, f - s)
        return abs(stones[0])
