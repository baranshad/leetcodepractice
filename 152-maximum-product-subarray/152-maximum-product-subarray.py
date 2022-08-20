class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma = mi = 1
        ans = float(-inf)
        for i in nums:
            mi, ma = min(i, ma*i, mi*i), max(i, ma*i, mi*i)
            ans = max(ans, mi, ma)
        return ans 
            
        