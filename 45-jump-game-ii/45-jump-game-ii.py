class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0 
        j = 1 
        count = 0
        while j < len(nums):
            i, j = j, max(nums[i]+ i +1 for i in range(i,j))
            count += 1 
        return count 