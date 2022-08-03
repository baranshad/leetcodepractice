class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        left = 0
        right = len(nums)-1
        while left < right:
            sum1 = nums[left] + nums[right]
            if sum1 < k:
                ans = max(ans, sum1)
                left += 1 

            else:
                right -= 1 
            
        return ans 