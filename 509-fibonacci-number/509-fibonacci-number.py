class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n==1:
            return n 
        ans = [0,1]
        for i in range(2,n+1):
            temp = ans[-1] + ans[-2]
            ans.append(temp)
            
        return ans[-1]