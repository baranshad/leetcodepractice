class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start = 0
        nums = nums+[-1]
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i] + 1:
                if start != i:
                    res.append(str(nums[start])+"->"+str(nums[i]))
                    start = i+1 
                else:
                    res.append(str(nums[i]))
                    start = i+1 
        return res 
    
    
