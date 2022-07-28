class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c_set = len(set(candyType))
        maxn = len(candyType) //2 
        return min(c_set, maxn)