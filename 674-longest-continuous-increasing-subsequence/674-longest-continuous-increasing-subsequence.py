class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1 
        res = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                ans += 1 
                res = max(res, ans)
            else:
                ans = 1 
            
        return res 