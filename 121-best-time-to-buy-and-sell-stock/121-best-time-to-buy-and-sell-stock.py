class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        start = prices[0]
        for i in prices[1:]:
            if i < start:
                start = i 
            ans = max(ans, i-start)
        return ans 