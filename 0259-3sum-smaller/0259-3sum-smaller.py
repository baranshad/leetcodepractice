class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: 
            return 0 
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            left = i + 1 
            right = len(nums) -1 
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 < target:
                    res += right - left 
                    left += 1 
                else:
                    right -= 1 
                
        return res 
 
 
  