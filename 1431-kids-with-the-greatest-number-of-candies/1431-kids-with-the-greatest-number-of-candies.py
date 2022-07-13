class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxc = max(candies)
        res = []
        for i in candies:
            res.append(i+extraCandies >= maxc)
            
        return res 