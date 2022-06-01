class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        length = 0 
        for i in nums:
            if i == 0:
                length = 0 
            else:
                length += 1 
                ans = max(ans, length)
                
        return ans 
        
        
        
       