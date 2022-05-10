class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(stack, used):
            if len(stack) == len(nums):
                res.append(stack[:])
                
            for i in range(len(nums)):
                if used[i] == True:
                    continue 
                used[i] = True 
                stack.append(nums[i])
                helper(stack, used)
                stack.pop()
                used[i] = False 
                
        helper([], [False]*len(nums))
        return res 