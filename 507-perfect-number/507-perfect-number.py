class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        
        #factors = list(set(x for tup in ([i, num//i] for i in range(1, int(num**0.5)+1) if num % i == 0) for x in tup))
        factorset = set()
        for i in range(1, int(num**0.5)+1):
            if num % i ==0:
                factorset.add(i)
                factorset.add(num//i)
        
        factorset.remove(num)
        return sum(factorset) == num