class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c1 = Counter(words[0])
        print(c1)
        for i in words[1:]:
            c1 = {x:min(Counter(i)[x],c1[x]) for x in c1 if x in Counter(i)}
        
        print(c1)
        res = []
        for i, j in c1.items():
            res.extend(i*j)
        
        return res