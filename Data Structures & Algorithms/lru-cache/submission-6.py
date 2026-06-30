class NodeList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}
        self.head = NodeList(0, 0)
        self.tail = NodeList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.add_head(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        
        curNode = NodeList(key, value)
        self.add_head(curNode) 
        self.hashmap[key] = curNode

        if len(self.hashmap) > self.cap:
            delNode = self.tail.prev
            self.remove(delNode)
            del self.hashmap[delNode.key]
