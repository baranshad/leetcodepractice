class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0 
        partialsum =  {}
        partialsum[0] = 1 
        pre = 0
        for i in nums:
            pre = pre + i 
            
            if pre - k in partialsum:
                ans += partialsum[pre-k] 
            
            partialsum[pre] = partialsum.get(pre,0) + 1 
        return ans 
 

