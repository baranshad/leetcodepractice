class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i,val in enumerate(keyboard):
            d[val] = i
        ans = d[word[0]]
        for i in range(len(word)-1):
            ans += abs(d[word[i+1]] - d[word[i]])
        return ans 
            
        
        