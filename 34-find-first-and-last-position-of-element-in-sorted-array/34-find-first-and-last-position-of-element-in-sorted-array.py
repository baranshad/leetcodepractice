class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        r = len(nums) -1 
        while l <= r:
            mid = l + (r-l)//2 
            if nums[mid] == target:
                pr = mid 
                pl = mid
                while pr < r and nums[pr+1] == target:
                    pr += 1 
                while nums[pl-1] == target and pl > 0 :
                    pl -= 1 
                    
                return [pl, pr]
            
            elif nums[mid] < target:
                l = mid +1 
            else:
                r = mid -1 
                
        return [-1, -1]
    
                
                
                    