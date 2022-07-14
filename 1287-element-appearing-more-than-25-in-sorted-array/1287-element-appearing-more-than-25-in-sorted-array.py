class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        res = [i for i, j in c.items() if j > 0.25*(len(arr))]
        return res[0]