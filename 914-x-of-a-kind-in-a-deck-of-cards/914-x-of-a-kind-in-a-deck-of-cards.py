class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            while b: 
                a, b = b, a % b
            return a
        print(reduce(gcd, Counter(deck).values()))
        return reduce(gcd, Counter(deck).values()) > 1