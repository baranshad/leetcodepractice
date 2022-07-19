class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        p = len(s) - 1
        while p >= 0:
            if s[p] == ' ':
                if l > 0:
                    return l
            else:
                l += 1
            p -= 1
        return l
        
       