class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) -1 
        if n == 0:
            return nums 
        if nums[-1] > nums[-2]:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return 
        p= 0 
        for i in range(n, 0, -1):
            if nums[i] > nums[i-1]:
                p = i 
                break 
        if p == 0:
            nums.sort()
            return 
        elif p > 0:
            j = len(nums) -1 
            while nums[p-1] >= nums[j]:
                j -= 1 
            nums[p-1], nums[j] = nums[j], nums[p-1]
            nums[p:] = sorted(nums[p:])
                