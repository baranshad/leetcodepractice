class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i,val in enumerate(keyboard):
            d[val] = i
        #print(d)
        prev = 0
        ans = 0
        for i in word:
            ans += abs(prev-d[i])
            prev = d[i]
        return ans 
            
        
        