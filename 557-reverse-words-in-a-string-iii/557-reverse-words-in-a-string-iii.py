class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0 
        l = 0
        s = s + " "
        r = len(s) -1 
        temp = ""
        while i <= r:
            if s[i] ==" " or i == r:
                temp += "".join(reversed(s[l:i+1]))
                i += 1 
                l = i 
            else:
                i += 1 
        return temp[1:]
        

                 
        
        
                