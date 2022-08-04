class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        words.sort(key=len)
        for i, val in enumerate(words):
            for word in words[i+1:]:
                if val in word:
                    res.add(val)
        return list(res)
        
        
        #ret = set()
        
        #words.sort(key=len)
        #for i, pattern in enumerate(words):
            #for word in words[i + 1:]:       
                #if pattern in word:
                    #ret.add(pattern)
        #return list(ret)
        
        
        #out = []
        #total = '_'.join(words)
        #for i in words:
            #occurance = total.count(i)
            #if occurance >1:
                #out.append(i)
        #return out