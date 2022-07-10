class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum = [0]
        s = 0
        for i in nums:
            s += i
            presum.append(s)
        presum.append(0)    
        for i in range(1, len(nums)+1):
            if presum[i-1] == presum[-2]- presum[i]:
                return i-1
        return -1