class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s) 
        ans = 0 
        i = 0 
        j = 0 
        word_freq = defaultdict()
        while j < len(s):
            word_freq[s[j]] = j
                
            if len(word_freq) == 3:
                delidex = min(word_freq.values()) 
                del word_freq[s[delidex]] 
                i = delidex + 1 
                print(i,j)
            ans = max(ans, j-i + 1)
                
            j += 1 
            
        return ans 


            