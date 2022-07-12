class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        e = o = 0
        for i in position:
            if i % 2 == 0:
                e += 1 
            else:
                o += 1 
                
        return min(e,o)