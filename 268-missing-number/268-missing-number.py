class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_s = sorted(nums)
        print(nums_s)
        for i,v in enumerate(nums_s):
            if i!= v:
                print(i,v)
                return i
        return len(nums)