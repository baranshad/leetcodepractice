class Solution:
    def sortString(self, s: str) -> str:
        c = Counter(s)
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        reverse_alpha = alphabets[::-1]
        res = ""
        count = len(s)
        while count > 0:
            for i in alphabets:
                if c[i]:
                    count -=1 
                    res += i 
                    c[i] -= 1 
            for j in reverse_alpha:
                if c[j]:
                    count -=1 
                    res+= j
                    c[j] -=1 
        return res 

                    
            
    