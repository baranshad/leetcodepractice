class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            if val in d:
                d[val] +=1 
            else:
                d[val] = 1 
                
        res = [i for i in d if d[i] > 1]
        return res
            