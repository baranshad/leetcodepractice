class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float("inf")
        nums.sort()
        for i in range(len(nums)):
            cur = nums[i]
            l = i+1 
            r = len(nums)-1 
            while l < r:
                sum3 = cur + nums[l] + nums[r]
                if abs(sum3 - target) < abs(ans):
                    ans = target - sum3 
                if sum3 < target:
                    l += 1 
                else:
                    r -= 1 
            if ans == 0:
                break 
                
        return target - ans 