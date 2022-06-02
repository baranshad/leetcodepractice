class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        
        ans = [i for (i,j) in d.items() if j==1]
        return ans[0]