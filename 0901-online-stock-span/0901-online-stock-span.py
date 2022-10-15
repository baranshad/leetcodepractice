class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        counter = 1 
        while self.stack and self.stack[-1][0] <= price:
            counter += self.stack.pop()[1]
        self.stack.append((price,counter))
        return counter 


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


## input [100,80,60,70,60,75,85]
## 100, 
## put 100 into store [(100,1)]  
## 80 < 100, [(100,1), (80,1)]
## 60 < 80, [(100,1),(80,1),(60,1)]
## 70 > 60, [(100,1),(80,1), (70,2)], store [(60,1)]
## 60 < 70, [(100,1),(80,1), (70,2)], store [(60,1), (60,1)]

## 75 > 70, [(100,1),(80,1), (75,len(store)+1)], [(60,1),(70,2),(60,1)]
## 85 > 75, [(100,1),(80,1),(85,)], pop(75),  [(60,1),(70,2),(60,1),(75,4)]
## 85 > 80, [(100,1),(85,6)], pop(80), [(60,1),(70,2),(60,1),(75,4),(80,1)]

 