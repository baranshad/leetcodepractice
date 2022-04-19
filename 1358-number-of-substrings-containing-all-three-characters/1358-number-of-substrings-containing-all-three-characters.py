class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0 
        j = 0 
        ans = 0
        word_freq = {'a':0,'b':0,'c':0}
        while j < len(s):
            word_freq[s[j]] += 1 
                
            while all(word_freq.values()) :
                ans += len(s) - j 
                word_freq[s[i]] -= 1 
                i += 1 
            

            j += 1 
            
        return ans 
    

       