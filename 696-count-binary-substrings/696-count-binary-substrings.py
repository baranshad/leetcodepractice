class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(len(s)-1):
            if s[i+1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1 
                
        return sum(min(groups[i], groups[i+1]) for i in range(len(groups)-1))
                
 