class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s_s = sorted(nums, reverse=True)
        ans = 0
        i = 0
        while i < len(nums)-1:
            ans += min(s_s[i], s_s[i+1])
            print(ans)
            i += 2
            
        return ans 