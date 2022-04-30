class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, i, ans):
            left = i+1 
            right = len(nums) -1 
            while left < right:
                sumofthree = nums[i] + nums[left] + nums[right]
                if sumofthree < 0:
                    left +=1 
                elif sumofthree > 0:
                    right -= 1 
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left +=1 
                    right -=1 
                    while left < right and nums[left] == nums[left-1]:
                        left +=1 
                        
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0: break 
            elif i==0 or nums[i] != nums[i-1]:
                helper(nums, i, ans)              
        return ans 

            
        