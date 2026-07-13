class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        # counts_from_list = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
        # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})
        count = Counter(tasks)
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)
        coolList = deque() #[-cnt, idletime]

        while coolList or maxHeap:
            time += 1
            if maxHeap:
                cnt = int(heapq.heappop(maxHeap)) + 1 #each task count -1
                if cnt != 0:
                    coolList.append([cnt, time + n])
            else:
                time = coolList[0][1]
            if coolList and coolList[0][1] == time:
                heapq.heappush(maxHeap,coolList.popleft()[0])
        return time


