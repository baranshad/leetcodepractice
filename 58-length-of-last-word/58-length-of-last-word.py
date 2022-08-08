class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        p = len(s)-1
        while p >=0:
            if s[p] ==" ":
                if count > 0:
                    return count 
            else:
                count += 1 
            p -= 1 
        return count 
       
       