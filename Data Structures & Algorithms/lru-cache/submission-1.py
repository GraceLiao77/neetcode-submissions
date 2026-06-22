from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.mapdict = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.mapdict:
            self.mapdict.move_to_end(key) # 移到最后
            return self.mapdict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.mapdict[key] = value
        self.mapdict.move_to_end(key)
        if self.cap < len(self.mapdict):
            self.mapdict.popitem(last=False)
