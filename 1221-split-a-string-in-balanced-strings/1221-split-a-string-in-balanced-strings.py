class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left = right = res = 0
        for c in s:
            if c == "L":
                left += 1 
            elif c == "R":
                right += 1 
            
            if left and right and left == right:
                res += 1 
                left = 0 
                right = 0
                
        return res 
        