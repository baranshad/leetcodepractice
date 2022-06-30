class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n> 0 and not n%2:
            return self.myPow(x*x,n//2)  
        elif n>0 and n%2:
            return x * self.myPow(x,n-1)
        else:
            return 1/self.myPow(x,-n)
        
    