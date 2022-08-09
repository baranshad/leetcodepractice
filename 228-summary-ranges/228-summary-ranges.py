class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        for j in range(len(nums)):
            if j == len(nums) -1 or nums[j+1] - nums[j] > 1:
                if i != j:
                    ans.append(str(nums[i]) + "->" + str(nums[j]))   
                else:
                    ans.append(str(nums[j]))
            
            
                i = j + 1 
            
        return ans 
            
            
          
      