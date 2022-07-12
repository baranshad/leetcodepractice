class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nc = {}
        arr= sorted(nums)
        res = []
        for i, n in enumerate(arr):
            if n not in nc:
                nc[n] = i 
            
        for j in nums:
            res.append(nc[j])
        return res 