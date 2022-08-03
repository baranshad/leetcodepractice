class Solution:
    def reverseWords(self, s: str) -> str:
        s += " "
        i = j = 0
        res = ""
        while i < len(s):
            if s[i] == " " or i == len(s)-1:
                res += "".join(s[j:i+1][::-1])
                i += 1 
                j = i
            else:
                i += 1 
                
        return res[1:]

 