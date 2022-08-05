class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedheight = sorted(heights)
        res = [i for i, j in zip(heights, sortedheight) if i != j]
        return len(res)