class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or (len(nums)==1 and target != nums[0]):
            return -1 
        
        l = 0 
        r = len(nums)-1 
        while l <= r:
            mid = l + (r-l)//2 
            if target == nums[mid]:
                return mid 
            
            if nums[mid] >= nums[l]:
                if nums[mid] >= target >= nums[l]:
                    r = mid -1 
                else:
                    l = mid + 1 
                    
            else:
                if nums[mid+1] <= target <= nums[r]:
                    l = mid + 1 
                else:
                    r = mid - 1 
                    
        return -1 