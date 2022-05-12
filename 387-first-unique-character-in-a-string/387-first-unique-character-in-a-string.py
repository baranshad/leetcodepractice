class Solution:
    def firstUniqChar(self, s: str) -> int:
        c =Counter(s)
        
        for i, val in enumerate(s):
            if val in c and c[val] == 1:
                return i 
        return -1 
             
            
        