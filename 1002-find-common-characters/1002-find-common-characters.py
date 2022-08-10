class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wordset1 = Counter(words[0])
        for i in words[1:]:
            wordset1 = {x: min(Counter(i)[x], wordset1[x]) for x in wordset1 if x in i}
        res = []
        for i, j in wordset1.items():
            res.extend(i*j)
        return res 
    
   