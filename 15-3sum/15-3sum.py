class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = [] 
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                cur = nums[i]
                l = i+1 
                r = len(nums)-1 
                while l < r:
                    three = cur + nums[l] + nums[r]
                    if three == 0:
                        res.append([cur, nums[l], nums[r]])
                        l += 1 
                        r -= 1 
                        continue
                    if three < 0:
                        l += 1 
                    else:
                        r -= 1 
        return [x for x in set(tuple(x) for x in res)]
      
             