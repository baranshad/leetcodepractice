class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = hold = float("-inf")
        reset = 0 
        for i in prices:
            pre_sold = sold 
            sold = hold + i 
            hold = max(hold, reset - i)
            reset = max(reset, pre_sold)
            
        return max(reset, sold)