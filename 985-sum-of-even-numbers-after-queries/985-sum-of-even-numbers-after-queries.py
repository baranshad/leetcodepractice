class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        s= sum(x for x in nums if x%2 == 0) 
        for i, j in queries:
            if nums[j] % 2 ==0:
                s -= nums[j]
            nums[j] = nums[j]+i
            if (nums[j]) % 2 ==0:
                s += nums[j] 
            res.append(s)
            
        return res