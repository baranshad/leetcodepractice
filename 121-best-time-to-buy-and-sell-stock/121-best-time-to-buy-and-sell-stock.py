class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        basevalue = prices[0]
        for i in prices[1:]:
            if i < basevalue:
                basevalue = i 
            else:
                ans = max(ans, i-basevalue)
            
        return ans 
                