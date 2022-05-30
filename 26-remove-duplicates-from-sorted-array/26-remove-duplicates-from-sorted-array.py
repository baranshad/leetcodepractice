class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0 
        j = 1 
        while j < len(nums):
            if nums[j] != nums[idx]:
                idx += 1 
                nums[idx] = nums[j]
            j +=1 
        return idx + 1 