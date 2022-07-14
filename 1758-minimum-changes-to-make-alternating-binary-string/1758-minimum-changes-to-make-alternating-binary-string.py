class Solution:
    def minOperations(self, s: str) -> int:
        slist = list(s)
        
        sint = [int(val) for i, val in enumerate(slist) if i %2 == 0]
        sint_odd = [int(val) for i, val in enumerate(slist) if  i %2 == 1]
        n = len(sint)
        m = len(sint_odd)
        return min(n - sum(sint) + sum(sint_odd) , sum(sint) + m - sum(sint_odd))
        