class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        ans = 0
        for j in prices:
            if j < start:
                start = j 
            ans = max(ans, j - start)
        return ans 