class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        ans = max(nums)
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                res += nums[i+1]
                
            else:
                res = nums[i+1]
            ans = max(ans, res)
                
        return ans 
        
        
        
        #maxSum = max(nums)
        #curr = nums[0]
        
        #for i in range(len(nums) - 1):
            #if nums[i] < nums[i + 1]:
                #curr += nums[i + 1]
            #else:
                #curr = nums[i + 1]
            
            #maxSum = max(curr, maxSum)

                
        #return maxSum
                