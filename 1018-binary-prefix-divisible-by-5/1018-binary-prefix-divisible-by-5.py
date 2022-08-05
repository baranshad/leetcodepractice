class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = 0 
        res = []
        for i in nums:
            ans = ans* 2 + i 
            res.append(ans)
        
        return [not i%5 for i in res]
                
                
                
                
    