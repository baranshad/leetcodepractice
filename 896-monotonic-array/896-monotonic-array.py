class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def helper(s):
            for i in range(len(s)-1):
                if s[i] < s[i+1]:
                    return False 
            return True
        
        return helper(nums) or helper(nums[::-1])