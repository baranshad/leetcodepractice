class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2 
            if nums[mid] == target:
                lm = mid
                rm = mid 
                while lm > 0 and nums[lm-1] == target:
                        lm -= 1 
                while rm < right and nums[rm+1] == target:
                        rm += 1 
                return [lm,rm]
            
            elif nums[mid] < target:
                left = mid+1 
                
            else:
                right = mid - 1 
                
                
        return [-1,-1]
                    