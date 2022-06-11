class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        
        left = 1
        right = x 
        while left <= right:
            mid = left + (right-left)//2 
            temp = mid * mid
            if temp == x:
                return int(mid)
            elif temp < x:
                left = mid +1 
            else:
                right = mid -1 
        print(left, right)
        return right
                
                
            
         
            