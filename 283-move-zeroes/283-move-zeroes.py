class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0 
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[start],nums[j] = nums[j], nums[start]
                start += 1 
                
            
            
        