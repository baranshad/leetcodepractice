class Solution:
    def checkRecord(self, s: str) -> bool:
        c1 = c2 = maxc2 = 0
        s1 = s + "P"
        print(s1)
        for i in range(len(s1)-1):
            if s1[i] == s1[i+1] and s1[i]== "L":
                c2 += 1 
            else:
                c2 = 0
                if s1[i] == "A":
                    c1 += 1
            maxc2 = max(maxc2, c2+1)
        return c1 < 2 and maxc2 < 3