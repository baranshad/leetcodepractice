class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] +=1 
            else:
                d[i] = 1 
                
        res = [i for i, j in d.items() if j> int(len(nums)/2)]
        return res[0]