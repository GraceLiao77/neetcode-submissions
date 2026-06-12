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
            return cur[cur.keys()[idx]] 
            # iloc 是 SortedDict / SortedList 的按位置索引
            # 普通 dict 不能按"第几个"访问，但 SortedDict 可以用 iloc 拿到第 n 个 key
        '''
        sd = SortedDict()
        sd[1] = 'val1'
        sd[3] = 'val3'
        sd[5] = 'val5'

        # 找 <= 4 的最大 key
        idx = sd.bisect_right(4)   # 返回 2（插入位置）
        key = sd.iloc[idx - 1]     # sd.iloc[1] = 3 ✅
        sd[key]                    # 'val3'
        '''
