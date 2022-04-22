class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(idx, temp):
            ans.append(temp[:])
            for i in range(idx, len(nums)):
                temp.append(nums[i])
                helper(i+1, temp)
                temp.pop()
                    
        helper(0, [])
        return ans 