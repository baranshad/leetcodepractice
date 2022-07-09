class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        ans = 0
        for i in prices:
            if i < start:
                start = i
            ans=max(ans, i-start)
            
        return ans 
                