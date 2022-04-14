class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1
        n = len(nums)
        l = 0 
        r = n -1 
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                l = mid + 1    
            elif nums[mid] > target:
                r = mid -1 
                
        return -1 

    