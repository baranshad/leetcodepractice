class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n ==2:
            return n 
        
        count = [1,2]
        for i in range(2,n):
            count.append(count[-1] + count[-2])
            
        return count[-1]