class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(temp, used):
            if len(temp)== len(nums):
                res.append(temp[:])
            for i in range(len(nums)):
                if used[i] == True:
                    continue 
                used[i] = True 
                temp.append(nums[i])
                helper(temp, used)
                temp.pop()
                used[i] = False
        helper([], [False]*len(nums))
        return res 