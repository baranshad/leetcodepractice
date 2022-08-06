class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        arr = sorted(nums)
        res = []
        for i, val in enumerate(arr):
            if val not in d:
                d[val] = i ## this is updateing the ranks 
        
        return [d[i] for i in nums]
            
            