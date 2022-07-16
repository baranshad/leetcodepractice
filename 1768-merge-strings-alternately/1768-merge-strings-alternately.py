class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))
        res = []
        for i in range(m):
            res.append(word1[i])
            res.append(word2[i])
            
        if len(word1) > m:
            return "".join(res) + word1[m:]
        
        elif len(word2) > m:
            return "".join(res) + word2[m:]
        
        else:
            return "".join(res)