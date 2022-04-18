class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0 
        partialsum = defaultdict(int)
        pre = 0
        for i in nums:
            pre = pre + i 
            if pre == k:
                ans += 1 
            
            if pre - k in partialsum:
                ans += partialsum[pre-k] 
            
            partialsum[pre] += 1 
        return ans 
 
    
