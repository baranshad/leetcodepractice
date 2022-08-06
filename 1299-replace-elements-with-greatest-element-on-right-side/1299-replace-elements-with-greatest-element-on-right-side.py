class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        for i in range(len(arr)-1, -1, -1):
            if res and arr[i] > res[-1]:
                res.pop()
                res.append(arr[i])
            res.append(res[-1])
        ans = [-1] + res
        return ans[:len(arr)][::-1]
                