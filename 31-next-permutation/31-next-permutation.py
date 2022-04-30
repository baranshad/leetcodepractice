class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt = 0 
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                pt = i 
                break
        
        if pt == 0:
            nums.sort()
            return 
        j = len(nums) -1
        while nums[pt-1] >= nums[j]:
            j -=1 
            
        nums[pt-1], nums[j] = nums[j], nums[pt-1]
        nums[pt:] = reversed(nums[pt:])
            
        
    

  