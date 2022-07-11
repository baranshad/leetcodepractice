class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = 0 
        transfer = []
        for i in nums:
            ans = ans*2 + i
            transfer.append(ans)
        res = [i%5==0 for i in transfer]
        return res