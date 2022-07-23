class OrderedStream:

    def __init__(self, n: int):
        self.res = [None] * (n+1)
        self.start = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        self.res[idKey-1] = value
        res = []
        while self.res[self.start]:
            res.append(self.res[self.start])
            self.start += 1 
        return res 
        

