class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        target_word = Counter(chars)
        ans = 0 
        def helper(w, d):
            for i in w:
                if i not in d or d[i]== 0:
                    return 0 
                else:
                    d[i] -= 1 
            return len(w)
        
        #print(helper("dco", {"w":1, "o":1, "r":1,"d":2}))
        for i in words:
            ans += helper(i, target_word.copy())
            
        return ans 
    
    
  
    
            
        
        
    