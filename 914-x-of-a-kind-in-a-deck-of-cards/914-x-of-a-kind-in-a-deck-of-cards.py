class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            while b: 
                a, b = b, a % b
            return a
        return reduce(gcd, Counter(deck).values()) > 1