class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def helper(temp, idx):
            ans.append(temp[:])
            
            for i in range(idx, len(nums)):
                temp.append(nums[i])
                helper(temp, i+1)
                temp.pop()
                
            return ans 
        
        return helper([], 0)
                
            
            
            
            
            
## []
## 1- 12 - 123 
## 2 