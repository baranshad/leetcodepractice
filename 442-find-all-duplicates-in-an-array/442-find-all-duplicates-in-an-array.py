class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1 
            else:
                d[i] = 1
                 
                    
        res = [i for i, j in d.items() if j > 1]
        return res 