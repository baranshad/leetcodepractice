class Solution:
    def compress(self, chars: List[str]) -> int:
        s= f =0 
        n = len(chars)
        
        while f <n:
            chars[s] = chars[f]
            count = 1 
            while f < n-1 and chars[f] == chars[f+1]:
                count += 1 
                f += 1 
                
            if count > 1:
                for c in str(count):
                    chars[s+1] = c
                    s += 1 
                    
            f += 1 
            s += 1 
            
        return s 