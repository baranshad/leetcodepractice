class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(x,y):
            if y == 0:
                return x 
            return gcd(y,x%y)
        
        #vals = collections.Counter(deck).values()
        return (reduce(gcd, Counter(deck).values())) > 1