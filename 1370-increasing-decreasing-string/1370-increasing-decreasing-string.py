class Solution:
    def sortString(self, s: str) -> str:
        c = Counter(s)
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        rev_alphabets = alphabets[::-1]
        res = ""
        count = len(s)
        while count >0:
            for i in alphabets:
                if c[i]:
                    res+= i 
                    c[i] -= 1 
                    count -= 1 
            for j in rev_alphabets:
                if c[j]:
                    res+=j 
                    c[j] -= 1 
                    count -= 1 
        return res 
            
            
            
            
    