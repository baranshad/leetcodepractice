class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        
        factors = list(set(x for tup in ([i, num//i] for i in range(1, int(num**0.5)+1) if num % i == 0) for x in tup))
        sumfactors = sum(factors) - num
        if num % 2 != 0:
            return False
        else:
            if num == sumfactors:
                return True
            else:
                return False