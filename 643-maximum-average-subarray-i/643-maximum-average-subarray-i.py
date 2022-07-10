class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        parsum = 0
        ans = float("-inf")
        i = 0
        for j in range(len(nums)):
            parsum += nums[j]
            if j-i+1 == k:
                ans = max(ans, parsum)
                parsum -= nums[i]
                i+=1 
        return ans/k
            
        
     