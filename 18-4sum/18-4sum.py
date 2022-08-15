class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twosum(nums, target):
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or nums[i] != res[-1][1]:
                    if target - nums[i] in s:
                        res.append([target-nums[i], nums[i]])
                    s.add(nums[i])
            return res 
        
        def ksum(nums, target, k):
            res = []
            
            if not nums:
                return res 
            ave = target // k 
            if ave < nums[0] or nums[-1] < ave:
                return res 
            
            if k == 2: return twosum(nums, target)
            for i in range(len(nums)):
                if i ==0 or nums[i-1] != nums[i]:
                    for subset in ksum(nums[i+1:], target- nums[i], k-1):
                        res.append([nums[i]] + subset)
                        
            return res 
        
        nums.sort()
        return ksum(nums, target, 4)
        