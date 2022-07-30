class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        minvalue = float(inf)
        for i in nums:
            moves += i 
            minvalue = min(minvalue, i)
            
        return moves - minvalue * len(nums)