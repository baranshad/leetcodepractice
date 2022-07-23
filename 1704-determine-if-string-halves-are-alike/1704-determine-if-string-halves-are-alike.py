class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        d = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)
        l = s[:n//2]
        r = s[n//2:]
        
        counter1 = counter2 = 0
        for i in range((n//2)):
            if l[i] in d:
                counter1 +=1 
            if r[i] in d:
                counter2 += 1 
                
        return counter1 == counter2 