class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = 0 
        st =start
        for i in range(1,n):
            nums = start + 2*i 
            st ^= nums 
            
        return st 