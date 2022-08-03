class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, val in enumerate(nums):
            if leftsum == S - leftsum - val:
                return i 
            leftsum += val 
            
        return -1 
            