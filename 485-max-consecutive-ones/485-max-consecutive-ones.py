class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        j = 0 
        maxlength = 0 
        while j < len(nums):
            if nums[j] == 0:
                maxlength=0
            else:
                maxlength += 1 
                ans = max(ans, maxlength)
            j += 1 
        
        return ans
            
        
        
        
       