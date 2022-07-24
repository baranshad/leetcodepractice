class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0 
        temp = 0
        for i in nums:
            if i == 1:
                ans +=1 
            else:
                ans = 0
            temp = max(temp, ans)
            
        return temp 