class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        sd = sorted(d.items(), key=lambda x: (x[1],-x[0]))
        res = []
        for i,j in sd:
            res.extend([i]*j)
            
        return res 