class Solution:
    def check(self, nums: List[int]) -> bool:
        if sorted(nums) == nums:
            return True
        j = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                j = i 

        print(j)
        if j == len(nums)-1:
            return True
        else: 
            original = nums[j+1:] + nums[:j+1]
            return sorted(original) == original
      
                
        