class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        # 新的num放到minheap
        heapq.heappush(self.minheap, -num)
        # min最小值 > max最小值
        if self.minheap and self.maxheap and (-self.minheap[0] > self.maxheap[0]):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)
        # always keeping minheap is longer than maxheap
        if len(self.minheap) - len(self.maxheap) > 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)
        if len(self.maxheap) > len(self.minheap):
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -val)

    def findMedian(self) -> float:
        a = len(self.minheap)
        b = len(self.maxheap)
        print(self.minheap, self.maxheap)
        if (a + b) % 2 == 0:
            return float((-1 * self.minheap[0] + self.maxheap[0]) / 2)
        else:
            return float(-1 * self.minheap[0])

        
        