class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        target_char = Counter(chars)
        ans = 0 
        def helper(word, d):
            for i in word:
                if i not in d or d[i] ==0:
                    return 0
                else:
                    d[i] -= 1 
            return len(word)
        
        
        for i in words:
            ans += helper(i, target_char.copy())
            
        return ans 
    
    
  
    
            
        
        
    