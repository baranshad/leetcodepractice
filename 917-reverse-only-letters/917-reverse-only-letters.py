class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0 
        j = len(s)-1
        s1 = list(s)
        while i<j:
            if not s1[i].isalpha():
                i +=1 
            if not s1[j].isalpha():
                j -= 1 
            elif s1[i].isalpha() and s1[j].isalpha():
                s1[i], s1[j] = s1[j], s1[i]
                i+= 1 
                j -= 1 
                
        return "".join(s1) 