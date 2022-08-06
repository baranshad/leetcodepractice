class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s+= " "
        res = []
        temp = ""
        for i, val in enumerate(s):
            if val == " ":
                if len(temp) > 0:
                    res.append(temp)
                    temp = ""
            else:
                temp += val 
        
        return " ".join(res[:k])
                
 
            