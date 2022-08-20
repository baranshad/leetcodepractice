class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        rowindex = 1 
        while n > 0:
            n -= rowindex 
            rowindex += 1 
            if n >= 0:
                count += 1 
                
        return count 