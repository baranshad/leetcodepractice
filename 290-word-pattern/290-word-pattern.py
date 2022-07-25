class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        c = defaultdict(list)
        for i, val in enumerate(pattern):
            c[val].append(i)
                
        d = defaultdict(list)
        for i, val in enumerate(s.split()):
            d[val].append(i)
            
        c1 = [j for i,j in c.items()]
        c2 = [j for i, j in d.items()]
        
        return c1 == c2
        