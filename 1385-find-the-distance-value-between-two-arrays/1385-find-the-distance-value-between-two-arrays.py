class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        length = len(arr1)
        for n in arr1:
            for n2 in arr2:
                if not abs(n - n2) > d:
                    length -= 1
                    break
        return length