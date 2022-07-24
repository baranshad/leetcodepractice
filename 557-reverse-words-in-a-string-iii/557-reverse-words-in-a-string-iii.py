class Solution:
    def reverseWords(self, s: str) -> str:
        s += " "
        i = j = 0
        temp = ""
        while i < len(s):
            if s[i] == " " or i == len(s)-1:
                temp += "".join(s[j:i+1][::-1])
                i += 1 
                j = i 
            else:
                i += 1 
        return temp[1:]
        
        
                