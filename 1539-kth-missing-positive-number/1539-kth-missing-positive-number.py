class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arrfull = [i for i in range(1, len(arr)+k+1) if i not in arr]
        print(arrfull)
        return arrfull[k-1]