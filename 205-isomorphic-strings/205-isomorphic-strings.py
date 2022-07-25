class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 =defaultdict(list)
        c2 = defaultdict(list)
        for i in range(len(s)):
            if s[i] in c1:
                c1[s[i]].append(i)
            else:
                c1[s[i]] = [i]
                
        for i in range(len(t)):
            if t[i] in c2:
                c2[t[i]].append(i)
            else:
                c2[t[i]] = [i]
        c1_valuest = sorted([j for i, j in c1.items()])
        c2_valuest = sorted([j for i, j in c2.items()])
        
        return c1_valuest == c2_valuest
            