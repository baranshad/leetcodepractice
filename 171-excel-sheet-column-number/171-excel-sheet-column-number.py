class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        d = {chr(i + 65): i + 1 for i in range(26)}
        print(d)
        for i in range(len(columnTitle)):
            cur = columnTitle[len(columnTitle)-1 -i]
            res += d[cur] * (26**i)  
            
        return res 
   