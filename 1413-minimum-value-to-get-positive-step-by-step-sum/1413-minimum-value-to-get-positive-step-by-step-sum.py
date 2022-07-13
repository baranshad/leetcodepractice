class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 0
        temp = 0
        for i in nums:
            temp += i
            ans = min(ans, temp)
            print(ans)
        return 1 - ans  