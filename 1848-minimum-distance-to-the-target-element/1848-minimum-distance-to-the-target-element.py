class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = len(nums)
        for i, val in enumerate(nums):
            if val == target:
                res = min(abs(i-start), res)
                
        return res 
                