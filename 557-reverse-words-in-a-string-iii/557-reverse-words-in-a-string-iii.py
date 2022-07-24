class Solution:
    def reverseWords(self, s: str) -> str:
        s += " "
        ans = []
        temp = ""
        for i, val in enumerate(s):
            if val == " ":
                if len(temp) > 0:
                    ans.append(temp[::-1])
                    temp = ""
            elif val != " ":
                temp += val 
        return " ".join(ans)

                 
        
        
                