class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort it first, use the same trick as backtrack questions
        nums = sorted(nums) 
        res = [] 
        for i in range(len(nums)):# fix most left first, then adjust postions of l,r
            if i == 0 or nums[i] != nums[i-1]:# avoid repeat
                ## don't know why here [-2,0,0,2,2] doesn't work
                l = i+1 
                r = len(nums)-1 
                while l < r:
                    three = nums[i] + nums[l] + nums[r]
                    if three == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1 
                        r -= 1 
                        #continue
                    elif three < 0:
                        l += 1 
                    else:
                        r -= 1 
        print(res)
        return [x for x in set(tuple(x) for x in res)]
      
             