class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1 
            else:
                d[i] = 1 
                
        res = sorted(d.items(), key= lambda x: x[1], reverse=True)
        return res[0][0]