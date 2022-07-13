class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        d= {}
        for i, j in enumerate(nums):
            d[i] = j
        ds = sorted(d.items(), key=lambda x:(x[1]), reverse= True)
        print(ds)
        return (ds[0][1]-1)*(ds[1][1]-1)