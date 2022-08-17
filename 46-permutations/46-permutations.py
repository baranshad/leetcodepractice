class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(nums, idx):
            ans = []
            if idx >= len(nums):
                ans.append(nums[:])
                
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                ans+= helper(nums,idx+1 )
                nums[i], nums[idx] = nums[idx], nums[i]
            return ans
                
        
        
        return helper(nums, 0)