class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0,0]
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1 
                ans[0] = i 
            
            else:
                count[i] = 1 
                
        for j in range(l):
            if j+1 not in count:
                ans[1] = j+1 
                
        return ans 