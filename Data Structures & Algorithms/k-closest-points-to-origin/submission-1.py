class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            res = (x ** 2) + (y ** 2)
            minHeap.append([res, x, y])
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            r, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res

        # points.sort(key=lambda p: p[0]**2 + p[1]**2)
        # return points[:k]

