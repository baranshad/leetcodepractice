class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        ans = 0
        for num in nums:
            if nums_count[num+1]:
                ans = max(ans, nums_count[num]+nums_count[num+1])
                
        return ans 