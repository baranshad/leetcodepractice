class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()
     
    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)
        
    def popMax(self) -> int:
        maxvalue = max(self.stack)
        idx = len(self.stack) - 1
        while self.stack[idx] != maxvalue:
            idx -=1 
        del self.stack[idx]
        return maxvalue
        

    

    

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

## []
## [5] peekMax 5 , indx = 1
##[5,6] peekMax = max(val, 5) = 6, idx = 2
## [5, 6,6] peekMax = max(val, 6) = 6, idx = 3 