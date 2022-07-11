class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i, val in enumerate(arr):
            if i == val:
                return i 
        return -1