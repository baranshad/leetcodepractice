class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0 
        nums = [False, False] + [True] * (n-2)
        
        for p in range(2, int(sqrt(n))+1):
            if nums[p]:
                for mutiplies in range(p*p, n, p):
                    nums[mutiplies] = False 
                    
        return sum(nums)