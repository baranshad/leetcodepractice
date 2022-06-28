class Solution:
    def jump(self, nums: List[int]) -> int:
        # find the first position with nums[i] + i >= len(nums)
        # most attainable position 
        # 0: [1] 1: [2] 2:[3,4] 3 [4,5] find the idx 3, no need to go to idx 4 
        # just return len(d)
        # if can jump to nums[i] will always can jump to nums[i-1]
        start = 0
        end = 1
        count = 0
        
        while end <= len(nums)-1:
            start, end = end, max(nums[i]+i+1 for i in range(start, end))
            count += 1
            
        return count    
                
                