class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        ans = [0]*len(prices)
        for i in range(len(prices)-1, -1, -1):
            while res and prices[i] < res[-1]:
                res.pop()
            ans[i] = prices[i] - res[-1] if res else prices[i]
            res.append(prices[i])
        return ans 
      
        