class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float("inf")
        nums.sort()
        for i in range(len(nums)):
            l = i+1
            r = len(nums) -1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs(target - sum3) < abs(ans):
                    ans = target - sum3 
                if sum3 < target:
                    l += 1 
                else:
                    r -= 1 
            if ans ==0:
                break 
        return target - ans