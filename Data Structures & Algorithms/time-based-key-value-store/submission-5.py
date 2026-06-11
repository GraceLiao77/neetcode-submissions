from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.listmap = defaultdict(SortedDict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.listmap[key][timestamp] = value
        print(self.listmap)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.listmap:
            return ""
        else:
            cur = self.listmap[key]
            idx = cur.bisect_right(timestamp) - 1
            if idx < 0:
                return ""
            return cur[cur.iloc[idx]]
        
