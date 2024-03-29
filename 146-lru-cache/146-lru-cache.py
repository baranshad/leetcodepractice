class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1 
        else:
            value = self.d[key]
            self.d.move_to_end(key)
            return value 
            

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.move_to_end(key)
            
        self.d[key] = value 
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)