class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0 
        j = 0 
        parsum = 0
        ans = float(inf)
        while j < len(nums):
            parsum  = parsum + nums[j]
            while parsum >= target:
                ans = min(ans, j-i+1)
                parsum -= nums[i]
                i+=1 
            
            j +=1 
                
        return ans if ans != float(inf) else 0
 