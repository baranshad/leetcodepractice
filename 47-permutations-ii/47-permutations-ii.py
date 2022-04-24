class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def helper(temp, used):
            if len(temp) == len(nums):
                res.append(temp[:])
                
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1] and used[i-1] == False:
                    continue 
                if used[i] == False:
                    used[i] = True
                    temp.append(nums[i])
                    helper(temp, used)
                    temp.pop()
                    used[i] = False 
        helper([], [False]*len(nums))
        
        return res 