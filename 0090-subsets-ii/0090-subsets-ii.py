class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        temp = []
        
        def helper(idx):
            ans.append(temp[:])
            for i in range(idx, len(nums)):
                if i> idx and nums[i] == nums[i-1]:
                    continue 
                temp.append(nums[i])
                helper(i+1)
                temp.pop()
                
        helper(0)
        return ans 