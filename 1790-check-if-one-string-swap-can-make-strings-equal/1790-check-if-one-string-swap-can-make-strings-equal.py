class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        d=0
        diffs=[]
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                d+=1
                diffs.append(i)
                
        if d != 2 and d!= 0:
            return False 
        elif d== 0 or (d==2 and s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]]):
            return True 