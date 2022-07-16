class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        s= sum(x for x in nums if x%2 == 0) 
        for j, idx in queries:
            if nums[idx] % 2 == 0:
                s -= nums[idx]
            nums[idx] += j 
            if nums[idx] % 2 == 0:
                s += nums[idx]
            res.append(s)  
        return res 
            
                    