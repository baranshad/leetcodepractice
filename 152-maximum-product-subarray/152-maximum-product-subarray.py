class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxpro = minpro = 1 
        ans = float("-inf")
        for i in nums:
            minpro, maxpro = min(i, maxpro*i, minpro*i), max(i, maxpro * i, minpro * i)
            ans = max(ans, maxpro, minpro)
        return ans 
    
    