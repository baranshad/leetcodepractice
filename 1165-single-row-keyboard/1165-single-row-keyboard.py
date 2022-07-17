class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i,val in enumerate(keyboard):
            d[val] = i
        
        prev = 0
        res = 0
        for i in word:
            res += abs(prev-d[i])
            prev = d[i]
            
        return res 

         