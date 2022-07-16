class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            n= target - val
            if n not in seen:
                seen[val] = i
            else:
                return [seen[n], i]
            
            
      