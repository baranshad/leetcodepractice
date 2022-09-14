class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            n = target - val 
            if n in d:
                return [i, d[n]]
            else:
                d[val] = i